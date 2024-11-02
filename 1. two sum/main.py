from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
            Finds the indices of two numbers in an array that add up to a target.

            Args:
                nums: A list of integers.
                target: The target sum.

            Returns:
                A list containing the indices of the two numbers that sum to the target,
                or an empty list if no such pair exists.
        """
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []


