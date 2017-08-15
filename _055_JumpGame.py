class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        temp = 0
        for i in range(len(nums)-1):
            temp = max(temp, i + nums[i])
            if temp <= i:
                return False
        return True