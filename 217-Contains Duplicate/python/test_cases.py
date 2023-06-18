"""Tests the Contains Duplicate problem solutions and raises errors if test cases do not pass.
"""

import unittest
from solution import Solution


class TestTwoSumMethods(unittest.TestCase):
    """Testing the Contains Duplicate problem solutions.
    """

    def test_case1(self):
        """Test case 1 of the Contains Duplicate problem.
        """
        nums = [1,2,3,1]
        bool_out = Solution.contains_duplicate(nums=nums)
        self.assertEqual(True, bool_out)

    def test_case2(self):
        """Test case 2 of the Contains Duplicate problem.
        """
        nums = [1,2,3,4]
        bool_out = Solution.contains_duplicate(nums=nums)
        self.assertEqual(False, bool_out)

    def test_case3(self):
        """Test case 3 of the Contains Duplicate problem.
        """
        nums = [1,1,1,3,3,4,3,2,4,2]
        bool_out = Solution.contains_duplicate(nums=nums)
        self.assertEqual(True, bool_out)

if __name__ == '__main__':
    unittest.main()
