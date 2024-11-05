class Solution:
    def reverse(self, x: int) -> int:

        if x < -1 * 2 ** 31 or x > 2 ** 31 - 1:
            return 0

        reversed_int = 0
        store_sign = True if x < 0 else False
        x = abs(x)

        # Loop until the input integer is greater than 0
        while x > 0:
            # Get the last digit of the input integer
            last_digit = x % 10

            # Add the last digit to the reversed integer
            reversed_int = (reversed_int * 10) + last_digit

            # Remove the last digit from the input integer
            x = x // 10

        if reversed_int < -1 * 2 ** 31 or reversed_int > 2 ** 31 - 1:
            return 0

        # Return the reversed integer
        return reversed_int * -1 if store_sign else reversed_int


sol = Solution()
print(sol.reverse(-123))