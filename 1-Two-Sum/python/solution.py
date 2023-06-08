"""Script used to solve the two sum problem
"""

from typing import List, Tuple


class Solution():
    """Implements methods for solving the two sum problem.
    """

    @staticmethod
    def two_sum(target: int, arr: List[int]) -> Tuple[int, int]:
        """Outputs solution to the two sum problem.

        Args:
            target (int): target value of the two sum problem
            arr (List[int]): set of numbers for the two sum problem

        Returns:
            Tuple[int, int]: indices of the set that solve the two sum problem
        """
        for n_idx, n_val in enumerate(arr):
            for m_idx, m_val in enumerate(arr):
                if n_idx != m_idx and n_val + m_val == target:
                    return n_idx, m_idx
