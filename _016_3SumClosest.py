class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # sort the array list
        nums.sort()
        dist = (1 << 31) - 1
        result = 0
        for i in range(0, len(nums) - 2):
            sum = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if abs(sum - target) < dist:
                    dist = abs(sum - target)
                    result = sum
                if sum <= target:
                    left += 1
                else:
                    right -= 1
        return result
