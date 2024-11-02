import unittest
from main import Solution

class TestTwoSum(unittest.TestCase):

    def test_two_sum_example_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected_indices = [0, 1]
        self.assertEqual(Solution().twoSum(nums, target), expected_indices)

    def test_two_sum_example_2(self):
        nums = [3, 2, 4]
        target = 6
        expected_indices = [1, 2]
        self.assertEqual(Solution().twoSum(nums, target), expected_indices)

    def test_two_sum_example_3(self):
        nums = [3, 3]
        target = 6
        expected_indices = [0, 1]
        self.assertEqual(Solution().twoSum(nums, target), expected_indices)

    def test_no_solution(self):
        nums = [1, 2, 3, 4, 5]
        target = 10
        expected_indices = []
        self.assertEqual(Solution().twoSum(nums, target), expected_indices)

if __name__ == '__main__':
    unittest.main()