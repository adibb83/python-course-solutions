import unittest

from HW2.solutions.git_CLI_command_simulator import git_command_simulator


class TestGitCommandSimulator(unittest.TestCase):
    def test_git_add(self):
        self.assertEqual(git_command_simulator("git add file.txt"),
                         "Stage all changes or specific file file.txt for the next commit.")

    def test_git_rm(self):
        self.assertEqual(git_command_simulator("git rm --cached file.txt"),
                         "Unstage file file.txt while retaining the changes in the working directory.")

    def test_git_commit(self):
        self.assertEqual(git_command_simulator("git commit -m 'initial commit'"),
                         "Commit changes to the repository with a descriptive message: 'initial commit'.")

    def test_git_push(self):
        self.assertEqual(git_command_simulator("git push"), "Upload your commits to the remote repository.")

    def test_git_stash(self):
        self.assertEqual(git_command_simulator("git stash"),
                         "Temporarily shelves changes in your working directory so you can work on a different task.")

    def test_git_stash_push(self):
        self.assertEqual(git_command_simulator("git stash push -m 'stash changes'"),
                         "Stashes changes with a custom message 'stash changes' for easy identification.")

    def test_git_stash_apply(self):
        self.assertEqual(git_command_simulator("git stash apply stash@{0}"),
                         "Applies the stashed changes with the specified name stash@{0}.")

    def test_invalid_command(self):
        self.assertEqual(git_command_simulator("invalid command"), "User input does not match any valid Git command")


# Run the unit tests
unittest.main()
