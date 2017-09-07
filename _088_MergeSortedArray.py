class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        index = m + n - 1
        m = m - 1
        n = n - 1
        while index >= 0:
            if n < 0:
                nums1[index] = nums1[m]
                m -= 1
            elif m < 0:
                nums1[index] = nums2[n]
                n -= 1
                print(nums1)
            elif nums1[m] > nums2[n] and m >= 0:
                nums1[index] = nums1[m]
                m -= 1
            else:
                nums1[index] = nums2[n]
                n -= 1
            index -= 1