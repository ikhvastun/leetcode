# ikh comment:
# idea is still to run 2 loops
# outer: run over all charachters
# inner: run over specific center
# i.e. aba -> #a#b#a#
# for #, a, # and b we run the whole inner loop
# P (at moment we identify the palindrome for b) [0, 1, 0, 3, >=0, >=1, >=0], 
# i.e. for second a no need to check for nearest charachters

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # trick to add # around every charachter
        # both even and odd strings will become odd
        s = "#" + "#".join(s) + "#"
        
        # define C, needed when will use mirror property
        C = 0

        # R will be used to define rightmost border to which
        # mirror property could be extended
        R = 0

        # define list for every charachter for which we store the longest 
        # palindrome
        P = [0] * len(s)
        
        for i in range(len(s)):
            # Here we define if we can use 
            # mirror property 
            if i < R:
                mirror_i = 2 * C - i
                P[i] = min(R - i, P[mirror_i])

            # define left and right charachter which we'll check
            a = i + (1 + P[i])
            b = i - (1 + P[i])

            # run inner loop, compare values to the left and right of i
            while a < len(s) and b >= 0 and s[a] == s[b]:
                P[i] += 1
                a += 1
                b -= 1

            # Here we redefine C and R
            if i + P[i] > R:
                C = i
                R = i + P[i]

        s = s.replace("#", "")
        max_length = max(P)
        center_index = P.index(max_length)
        start = (center_index - max_length) // 2
        end = start + max_length
        return s[start:end]

solution = Solution()
print(solution.longestPalindrome("abadaba"))