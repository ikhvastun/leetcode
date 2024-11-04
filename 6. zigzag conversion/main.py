class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        if len(s) <= numRows:
            return s

        rows = ["" for _ in range(numRows)]

        row, direction = 0, 1

        for i in s:
            rows[row] += i
            row += direction

            if row == numRows - 1:
                direction = -1
            elif row == 0:
                direction = 1

        return "".join(rows)


sol = Solution()
print(sol.convert("PAYPALISHIRING", 5))