import os


def git_command(command, args=[], path="."):
    final_command = f"git -C {path} {command}"
    print(final_command)
    return os.system(final_command)


def git_full_commit_command(commit_msg, commit_datetime, path):
    command_prefix = (
        'GIT_COMMITTER_DATE="{day} {day_num} {mon} {year} {hour}:{min}:{sec} BST" '
    )
    commit_command = 'git -C {path} commit -am "{message}" --date "{day} {day_num} {mon} {year} {hour}:{min}:{sec}"'
    full_command = command_prefix + commit_command
    command = full_command.format(
        day=commit_datetime.strftime("%a"),
        day_num=commit_datetime.strftime("%d"),
        mon=commit_datetime.strftime("%b"),
        year=commit_datetime.year,
        hour=commit_datetime.hour,
        min=commit_datetime.minute,
        sec=commit_datetime.second,
        path=path,
        message=commit_msg,
    )
    os.system(command)


def git_add_all(path="."):
    return git_command(f"add {path}", path=path)


def git_add_file(path=".", file_path="."):
    command = "git -C {path} add .".format(path=path)
    print(command)
    return os.system(command)


def check_dir_valid_repo(dir_path):
    git_dir = f"{dir_path}/.git"
    return os.path.isdir(git_dir)


def check_dir_valid_repo_v2(dir_path):
    return git_command("status", path=dir_path) == 0


"""
git  -C /Users/ahmad/kitchen/leetcode add /Users/ahmad/kitchen/leetcode
git  -C /Users/ahmad/kitchen/leetcode add /Users/ahmad/kitchen/leetcode
"""
