class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        result = 1
        count = 1
        for i in range(1, n):
            if nums[i - 1] != nums[i]:
                nums[result] = nums[i]
                result += 1
                count = 1
            elif nums[i - 1] == nums[i] and count < 2:
                nums[result] = nums[i]
                result += 1
                count = 2
            else:
                count += 1
        return result