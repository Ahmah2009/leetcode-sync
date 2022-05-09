import sys
from lib.cookies_jar import load_cookies_jar
from lib.leetcode.request import LeetCodeRequest
from lib.config import ConfigReader


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Sync leetcode solutions",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("-l", "--limit")
    parser.add_argument("-o", "--offset")
    limit = 100
    offset = 0
    args = parser.parse_args()
    args = vars(args)
    if args["limit"] is not None:
        limit = int(args["limit"])

    if args["offset"] is not None:
        offset = int(args["offset"])

    config = ConfigReader()
    cookies_jar = load_cookies_jar(config.browser_name, "leetcode.com")
    leetcode_request = LeetCodeRequest(cookies_jar)
    leetcode_request.save_ac_solutions(
        repo_path=config.repo_path, limit=limit, offset=offset
    )
