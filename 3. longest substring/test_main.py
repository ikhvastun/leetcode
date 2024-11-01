import unittest
from main import Solution  # Assuming your code is in 'main.py'

class TestLongestSubstring(unittest.TestCase):

    def test_longest_substring(self):
        test_cases = [
            ("abcabcbb", 3),
            ("bbbbb", 1),
            ("pwwkew", 3),
            ("", 0),
            (" ", 1),
            ("au", 2),
            ("dvdf", 3),
            ("dvauvps", 5)
        ]
        for s, expected in test_cases:
            with self.subTest(s=s):
                self.assertEqual(Solution().lengthOfLongestSubstring(s), expected)

if __name__ == '__main__':
    unittest.main()
