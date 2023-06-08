"""Tests the two sum problem solutions and raises errors if test cases do not pass.
"""

import unittest
from solution import Solution


class TestTwoSumMethods(unittest.TestCase):
    """Testing the two sum problem solutions.
    """

    def test_case1(self):
        """Test case 1 of the two sum problem.
        """
        nums = [2,7,11,15]
        target = 9
        indices = Solution.two_sum(target=target, arr=nums)
        self.assertIsNotNone(indices)
        idx1, idx2 = indices
        two_sum = nums[idx1] + nums[idx2]
        self.assertEqual(target, two_sum)

    def test_case2(self):
        """Test case 2 of the two sum problem.
        """
        nums = [3,2,4]
        target = 6
        indices = Solution.two_sum(target=target, arr=nums)
        self.assertIsNotNone(indices)
        idx1, idx2 = indices
        two_sum = nums[idx1] + nums[idx2]
        self.assertEqual(target, two_sum)

    def test_case3(self):
        """Test case 3 of the two sum problem.
        """
        nums = [3,3]
        target = 6
        indices = Solution.two_sum(target=target, arr=nums)
        self.assertIsNotNone(indices)
        idx1, idx2 = indices
        two_sum = nums[idx1] + nums[idx2]
        self.assertEqual(target, two_sum)

if __name__ == '__main__':
    unittest.main()
