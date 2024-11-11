class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        # Convert the integer to a string and check if it's a palindrome
        return str(x) == str(x)[::-1]