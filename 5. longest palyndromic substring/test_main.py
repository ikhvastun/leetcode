import unittest
from main import Solution

class TestLongestPalindrome(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(Solution().longestPalindrome(""), "")

    def test_single_character(self):
        self.assertEqual(Solution().longestPalindrome("a"), "a")

    def test_even_length_palindrome(self):
        self.assertEqual(Solution().longestPalindrome("abba"), "abba")

    def test_odd_length_palindrome(self):
        self.assertEqual(Solution().longestPalindrome("racecar"), "racecar")

    def test_palindrome_at_beginning(self):
        self.assertEqual(Solution().longestPalindrome("levelradar"), "level")

    def test_palindrome_at_end(self):
        self.assertEqual(Solution().longestPalindrome("abccbadef"), "abccba")

    def test_multiple_palindromes(self):
        self.assertEqual(Solution().longestPalindrome("bananas"), "anana")

    def test_long_string(self):
        self.assertEqual(Solution().longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"), "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    
    def test_my_own_test(self):
        self.assertEqual(Solution().longestPalindrome("abadaba"), "abadaba")
        
if __name__ == '__main__':
    unittest.main()
