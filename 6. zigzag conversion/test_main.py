import unittest
from main import Solution

class TestZigZagConversion(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(Solution().convert("", 3), "")

    def test_single_character(self):
        self.assertEqual(Solution().convert("A", 1), "A")

    def test_numRows_1(self):
        self.assertEqual(Solution().convert("ABC", 1), "ABC")

    def test_numRows_equals_length(self):
        self.assertEqual(Solution().convert("ABCD", 4), "ABCD")

    def test_example_1(self):
        self.assertEqual(Solution().convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")

    def test_example_2(self):
        self.assertEqual(Solution().convert("PAYPALISHIRING", 4), "PINALSIGYAHRPI")

    def test_long_string(self):
        self.assertEqual(Solution().convert("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ", 5), "AIQYGOWBHJPRXZFHNPVXCGKOSWAEIMQUYDFLNTVBDJLRTZEMUCKS")

if __name__ == '__main__':
    unittest.main()
