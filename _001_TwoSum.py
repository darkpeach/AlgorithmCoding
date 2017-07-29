author = "Darkpeach"

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range (len(nums)):
            #print(i)
            if target - nums[i] in dict:
                return [dict[target - nums[i]], i]
            dict[nums[i]] = i
        return [-1, -1]

    def twoSumSortedArray(self, nums, target):
        l,r = 0, len(nums)-1
        while l<r:
            sum = nums[l] + nums[r]
            if sum == target:
                return [l,r]
            elif sum > target:
                r -= 1
            else:
                l +=1
        return []
