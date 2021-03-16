"""
Unittest cases for testing github API, and isolating external dependencies.
Author: NK
Date: 03/15/2021
"""


import unittest
from git_api import get_user_repos, get_commit_counts
from unittest.mock import MagicMock


class TestGitHubRepo(unittest.TestCase):
    """Test cases for github repo program"""

    def testUserRepo(self):
        mock = MagicMock()
        mock.__str__.return_value = '[hellogitworld, helloworld, Mocks, Project1, threads-of-life]'
        self.assertIn("SSW-567", get_user_repos("starkworld"))
        self.assertEqual(str(mock), '[hellogitworld, helloworld, Mocks, Project1, threads-of-life]')

    def testGetCommitCounts(self):
        mock = MagicMock()
        mock.__str__.return_value = '30'
        self.assertEqual(str(mock), '30')
        self.assertEqual(20, get_commit_counts("starkworld", "Student_DB_Repository"))


if __name__ == '__main__':
    print('Unittest are Running')
    unittest.main()
