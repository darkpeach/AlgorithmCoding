class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        maxSum = nums[0]
        minSum = 0
        maxSumIndex = 0
        minSumIndex = 0
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]
            if sums - minSum > maxSum:
                maxSum = sums - minSum
                maxSumIndex = i
            if sums < minSum:
                minSum = sums
                minSumIndex = i
        return maxSum