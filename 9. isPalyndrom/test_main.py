import unittest
from main import Solution

class TestSolution(unittest.TestCase):
    def test_positive_palindrome(self):
        sol = Solution()
        self.assertTrue(sol.isPalindrome(121))

    def test_negative_number(self):
        sol = Solution()
        self.assertFalse(sol.isPalindrome(-121))

    def test_not_palindrome(self):
        sol = Solution()
        self.assertFalse(sol.isPalindrome(10))

    def test_single_digit(self):
        sol = Solution()
        self.assertTrue(sol.isPalindrome(9))
