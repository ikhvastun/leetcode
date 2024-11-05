import unittest
from main import Solution

class TestReverseInteger(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(Solution().reverse(123), 321)

    def test_negative_integer(self):
        self.assertEqual(Solution().reverse(-123), -321)

    def test_zero(self):
        self.assertEqual(Solution().reverse(0), 0)

    def test_integer_with_trailing_zero(self):
        self.assertEqual(Solution().reverse(120), 21)

    def test_integer_overflow(self):
        self.assertEqual(Solution().reverse(1534236469), 0)

    def test_integer_underflow(self):
        self.assertEqual(Solution().reverse(-1563847412), 0)

if __name__ == '__main__':
    unittest.main()
