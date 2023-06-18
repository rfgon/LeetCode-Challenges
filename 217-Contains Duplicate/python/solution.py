"""Script used to solve the Contains Duplicate problem
"""

from typing import List


class Solution():
    """Implements methods for solving the Contains Duplicate problem.
    """

    @staticmethod
    def contains_duplicate(nums: List[int]) -> bool:
        """Outputs solution to the Contains Duplicate problem.

        Args:
            arr (List[int]): list of numbers for the Contains Duplicate problem

        Returns:
            bool: Boolean solution to the Contains Duplicate problem
        """
        array_set = set(nums)

        return len(nums) != len(array_set)
