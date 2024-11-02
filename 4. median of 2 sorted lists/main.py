from typing import List


# ikh comment:
# not clear at the beginning the solution
# but in the end it became much clearer
# idea behind is to find border where to split list A as quick as possible
# say list A = [1 4 5 6 9 20] and list B = [2 7 8 11 14 16]
# at first iteration the left pointer is assigned to 0 and right pointer is assiged to 5
# border is in the middle, i.e. A = [1 4 5 | 6 9 20], split on list B depends on total number of values, B = [2 7 8 | 11 14 16]
# at first guess we see that 5 < 11 (which is what we need), but 8 > 6, 
# which means that left highest value (one of two) is higher than smallest value of right part. Adjustment is needed
# l pointer is now assigned to smallest value of right part, i.e. 6, the border is now shifted
# A = [1 4 5 6 9 | 20], the border in B changes to adjust for equal number of numbers in left and right part, i.e.
# B = [2 | 7 8 11 14 16]. Compare values: 2 < 20, but 9 > 7, which means that we moved too far, right pointer needs to be adjusted. 
# r pointer now also points to position 3, border is now drawn as A = [1 4 5 6 | 9 20], B = [2 7 | 8 11 14 16]. 
# Split is done correctly.
# After there are just formalities, which depends on total number of values in 2 lists
# if number is even, we need to take max of left parts and min of right part and divide by 2
# Assume we have B = [2 7 8 11 14 16 17]
# Then split would be the following:
# iter1: A = [1 4 5 | 6 9 20], B = [2 7 8 | 11 14 16 17]
# iter2: A = [1 4 5 6 9 | 20], B = [2 | 7 8 11 14 16 17]
# iter3: A = [1 4 5 6 | 9 20], B = [2 7 | 8 11 14 16 17]
# we find the good split, as in right part we have 1 value more then median would be the smallest of right part 


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
       
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        total = len(nums1) + len(nums2)
        half = total // 2

        # pointers in the smallest list 
        l, r = 0, len(nums1) - 1
        while True:

            # here where we are going to split the smallest list
            i = (l + r) // 2  

            # here where we are going to split the largest list
            j = half - i - 2

            Aleft = nums1[i] if i >= 0 else float('-infinity')
            Aright = nums1[i + 1] if (i + 1) < len(nums1) else float('infinity')
            Bleft = nums2[j] if j >= 0 else float('-infinity')
            Bright = nums2[j + 1] if (j + 1) < len(nums2) else float('infinity')

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            # Here we need to adjust pointers in smallest lists 
            # if left border is larger than right border in list B
            # then we need to move right border in list A
            # this will adjust also border in list B but in next iteration 
            if Aleft > Bright:
                r = i - 1
            else:
                l = i + 1