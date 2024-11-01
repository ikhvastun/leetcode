class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        lp = 0
        longest = 0
        seen = set()

        for rp in range(len(s)):
            while s[rp] in seen:
                seen.remove(s[lp])
                lp += 1
            seen.add(s[rp])
            longest = max(longest, rp - lp + 1)

        return longest
    

sol = Solution()
print(sol.lengthOfLongestSubstring("pwwkew"))