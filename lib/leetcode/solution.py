import os
from datetime import datetime
from lib.leetcode.submission import Submission
from lib.git import git_full_commit_command, git_add_all, git_add_file


class Solution:
    def __init__(self, submission: Submission):
        self.submission = submission
        self.code = submission.code
        self.file_name = self._generate_file_name()
        self.solution_time = datetime.fromtimestamp(submission.timestamp)

    def _generate_file_name(self):
        problem_title = self.submission.title_slug
        solution_timestamp = self.submission.timestamp
        ext = self._get_solution_file_ext()
        return f"{problem_title}{solution_timestamp}.{ext}"

    def _get_solution_file_ext(self):
        solutions_ext = {
            "python": "py",
            "python3": "py",
            "erlang": "erl",
            "golang": "go",
            "javascript": "js",
        }
        if self.submission.lang in solutions_ext:
            return solutions_ext[self.submission.lang]
        return self.submission.lang

    def save_file(self, repo_path):
        path = "{path}/{title}/{file_name}".format(
            path=repo_path, title=self.submission.title_slug, file_name=self.file_name
        )
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))
        file = open(path, "w")
        file.write(self.code)
        file.close()
        git_add_file(path=repo_path, file_path=path)
        git_full_commit_command(self.get_commit_msg(), self.solution_time, repo_path)

    def get_commit_msg(self):
        return "Solve leetcode problem {title}".format(title=self.submission.title)
