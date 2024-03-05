class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()

        if len(nums1) % 2 != 0:
            mid = nums1[len(nums1) // 2]
            return float(mid)
        else:
            t = len(nums1) // 2
            median = (nums1[t] + nums1[t-1]) / 2
            return median
        
# runtime 74 ms Beats 88.16 of users with Python3
# space 16.88 Beats 87.40 of users with Python3