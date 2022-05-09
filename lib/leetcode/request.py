import requests
import time
from lib.constants import (
    LEETCODE_API_ALL_PROBLEMS,
    LEETCODE_API_ALL_PROBLEM_SUBMISSIONS,
)
from lib.errors import LeetcodeHTTPError
from lib.leetcode.submission import Submission
from lib.leetcode.solution import Solution


class LeetCodeRequest:
    def __init__(self, cookies_jar):
        self.cookies_jar = cookies_jar
        self.all_tried = []
        self.solved = []

    def request(self, url):
        response = requests.get(url, cookies=self.cookies_jar)
        if response.status_code != 200:
            print(response.status_code)
            raise LeetcodeHTTPError
        return response.json()

    def get_all_problems(self):
        all_problems_data = self.request(LEETCODE_API_ALL_PROBLEMS)
        all_problems = all_problems_data["stat_status_pairs"]
        return all_problems

    def get_all_solved_problems(self):
        all_problems = self.get_all_problems()
        return [p for p in all_problems if p["status"] == "ac"]

    def get_all_tried_problems(self) -> [dict]:
        all_problems = self.get_all_problems()
        return [p for p in all_problems if p["status"] is not None]

    def get_problem_submission_raw(self, problem_slug: str) -> [dict]:
        submissions = self.request(
            LEETCODE_API_ALL_PROBLEM_SUBMISSIONS.format(problem_slug=problem_slug)
        )
        return submissions["submissions_dump"]

    def get_problem_submissions(self, problem_slug: str) -> [Submission]:
        submissions_dump = self.get_problem_submission_raw(problem_slug)
        submissions = []
        for submission in submissions_dump:
            submissions.append(Submission(submission))
        return submissions

    def get_problem_solutions(self, problem_slug: str) -> [Solution]:
        submissions = self.get_problem_submissions(problem_slug)
        solutions = []
        for submission in submissions:
            one_solution = Solution(submission)
            solutions.append(one_solution)
        return solutions

    def get_all_ac_solutions(self, limit=10):
        solved = self.get_all_solved_problems()
        solutions = []
        for solved_problem in solved:
            print(solved_problem["stat"]["question__title_slug"])
            solutions.extend(
                self.get_problem_solutions(
                    solved_problem["stat"]["question__title_slug"]
                )
            )
            if not limit:
                break
            limit -= 1
            time.sleep(3)
        return solutions

    def save_ac_solutions(self, limit=10, repo_path=".", offset=0):
        count = 1
        solved = self.get_all_solved_problems()
        if offset != 0:
            solved = solved[offset:]
        for solved_problem in solved:
            print(count, solved_problem["stat"]["question__title_slug"])
            solutions = self.get_problem_solutions(
                solved_problem["stat"]["question__title_slug"]
            )
            for solution in solutions:
                solution.save_file(repo_path=repo_path)
            count += 1
            limit -= 1
            if not limit:
                break

            time.sleep(3)
