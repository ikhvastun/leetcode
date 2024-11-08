import unittest
from main import Solution

class TestSolution(unittest.TestCase):
    def test_positive_number(self):
        sol = Solution()
        self.assertEqual(sol.myAtoi("42"), 42)

    def test_negative_number(self):
        sol = Solution()
        self.assertEqual(sol.myAtoi("   -42"), -42)

    def test_number_with_trailing_words(self):
        sol = Solution()
        self.assertEqual(sol.myAtoi("4193 with words"), 4193)

    def test_words_and_number(self):
        sol = Solution()
        self.assertEqual(sol.myAtoi("words and 987"), 0)

    def test_large_negative_number(self):
        sol = Solution()
        self.assertEqual(sol.myAtoi("-91283472332"), -2147483648)

    def test_leading_zeros_with_negative(self):
        sol = Solution()
        self.assertEqual(sol.myAtoi("0-1"), 0)

    def test_plus_minus_sign(self):
        sol = Solution()
        self.assertEqual(sol.myAtoi("-+12"), 0)

    def test_minus_plus_sign(self):
        sol = Solution()
        self.assertEqual(sol.myAtoi("+-12"), 0)
    
    def test_empty_string(self):
        sol = Solution()
        self.assertEqual(sol.myAtoi(""), 0)

    def test_leading_whitespace(self):
        sol = Solution()
        self.assertEqual(sol.myAtoi("     123"), 123)

    def test_trailing_whitespace(self):
        sol = Solution()
        self.assertEqual(sol.myAtoi("123     "), 123)

    def test_leading_zeros(self):
        sol = Solution()
        self.assertEqual(sol.myAtoi("000123"), 123)

    def test_positive_sign(self):
        sol = Solution()
        self.assertEqual(sol.myAtoi("+123"), 123)

    def test_large_positive_number(self):
        sol = Solution()
        self.assertEqual(sol.myAtoi("2147483647"), 2147483647)

    def test_overflow_positive_number(self):
        sol = Solution()
        self.assertEqual(sol.myAtoi("2147483648"), 2147483647)

    def test_overflow_negative_number(self):
        sol = Solution()
        self.assertEqual(sol.myAtoi("-2147483649"), -2147483648)

    def test_float_number(self):
        sol = Solution()
        self.assertEqual(sol.myAtoi("-3.14"), -3)

    def test_only_minus(self):
        sol = Solution()
        self.assertEqual(sol.myAtoi("-"), 0)

    def test_zero_one_zero(self):
        sol = Solution()
        self.assertEqual(sol.myAtoi("010"), 10)

    def test_exotic(self):
        sol = Solution()
        self.assertEqual(sol.myAtoi("   +0 123"), 0)

if __name__ == '__main__':
    unittest.main()
