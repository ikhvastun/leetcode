from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        container_max = 0
        left, right = l, r
        
        while l != r:
            print("pos: ", l, r)

            container = min(height[l], height[r]) * (r - l)
            if container > container_max:
                print("cont and cont_max:", container, container_max)
                container_max = container
                left_max, right_max = l, r
            if height[l] <= height[r]:
                left += 1
            if height[l] > height[r]:
                right -= 1
            l, r = left, right
           

        return container_max, left_max, right_max

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea([1,8,6,2,5,4,8,3,7]))

