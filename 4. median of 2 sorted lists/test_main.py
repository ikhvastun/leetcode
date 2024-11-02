import unittest
from main import Solution 

class TestMedianSortedArrays(unittest.TestCase):

    def test_median_two_arrays(self):
        test_cases = [
            ([1, 4, 5, 6, 9, 20], [21, 22, 23], 9),
            ([1, 4, 5, 6, 9, 20], [3, 5, 7], 5),
            ([1, 3], [2], 2),
            ([1, 2], [3, 4], 2.5),
            ([0,0], [0,0], 0),
            ([],[1],1),
            ([2],[],2),
            ([1, 4, 5, 6, 9, 20], [2, 7, 8, 11, 14, 16], 7.5),
            ([1, 4, 5, 6, 9, 20], [2, 7, 8, 11, 14, 16, 17], 8),
        ]
        for nums1, nums2, expected_median in test_cases:
            with self.subTest(nums1=nums1, nums2=nums2):
                self.assertEqual(Solution().findMedianSortedArrays(nums1, nums2), expected_median)

if __name__ == '__main__':
    unittest.main()
