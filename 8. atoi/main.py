class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1  # 1 for positive, -1 for negative
        result = 0
        i = 0
        n = len(s)

        # 1. Ignore Leading Whitespace
        while i < n and s[i] == ' ':
            i += 1

        # 2. Determine Sign
        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        # 3. Read Digits and Handle Overflow
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # Check for overflow before multiplication
            if result > (2**31 - 1) // 10 or (result == (2**31 - 1) // 10 and digit > 7):
                return 2**31 - 1 if sign == 1 else -2**31

            result = result * 10 + digit
            i += 1

        return sign * result