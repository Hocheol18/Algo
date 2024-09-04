class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        length = len(nums1)
        return nums1[length//2] if length % 2 == 1 else (nums1[(length//2)-1] + nums1[length//2]) / 2.0