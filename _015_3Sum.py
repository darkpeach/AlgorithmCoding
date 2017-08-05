class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        # sort the list
        nums.sort()
        result = []
        for i in range(0, len(nums)-2):
            #ignore repeat first number, and filter out the very first if all number is equal to 0
            if i and nums[i] == nums[i-1]:
                continue
            print(nums[i])
            target = 0 - nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sums = nums[left] + nums[right]
                if sums == target:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sums < target:
                    left += 1
                else:
                    right -= 1
        return result
