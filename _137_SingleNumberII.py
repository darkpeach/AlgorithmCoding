class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one = 0
        two = 0
        for i in nums:
            one = (one ^ i) & ~ two
            two = (two ^ i) & ~ one
        return one