import re


def git_command_simulator(user_input: str) -> str:
    def check_strings_in_order(user_input, git_command):
        i, j = 0, 0

        while i < len(user_input) and j < len(git_command):
            if user_input[i] == git_command[j]:
                i += 1
            j += 1
        return i == len(user_input)

    # Define Git commands
    GIT_ADD = "git add"
    GIT_RM = "git rm --cached"
    GIT_COMMIT = "git commit -m"
    GIT_PUSH = "git push"
    GIT_STASH = "git stash"
    GIT_STASH_PUSH = "git stash push -m"
    GIT_STASH_APPLY = "git stash apply"

    user_input_arr = user_input.split()
    if check_strings_in_order(GIT_ADD.split(), user_input_arr):
        print(f'Stage all changes or specific file {user_input_arr[-1]} for the next commit.')
    elif check_strings_in_order(GIT_RM.split(), user_input_arr):
        print(f'Unstage file {user_input_arr[-1]} while retaining the changes in the working directory.')
    elif check_strings_in_order(GIT_COMMIT.split(), user_input_arr):
        print(f'Commit changes to the repository with a descriptive message: {" ".join(user_input_arr[3:])}.')
    elif check_strings_in_order(GIT_STASH_PUSH.split(), user_input_arr):
        print(f'Stashes changes with a custom message {" ".join(user_input_arr[4:])} for easy identification.')
    elif check_strings_in_order(GIT_STASH_APPLY.split(), user_input_arr):
        if len(user_input_arr) > 3:
            print(f'Applies the stashed changes with the specified name {" ".join(user_input_arr[3:])}.')
        else:
            print(f'Applies the most recently stashed changes.')
    elif check_strings_in_order(GIT_PUSH.split(), user_input_arr):
        print('Upload your commits to the remote repository.')
    elif check_strings_in_order(GIT_STASH.split(), user_input_arr):
        print('Temporarily shelves changes in your working directory so you can work on a different task.')
    else:
        print("User input does not match any valid Git command")


print("enter GIT command")
user_input = input()
result = git_command_simulator(user_input)

