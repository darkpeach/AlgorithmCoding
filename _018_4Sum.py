class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        if not nums:
            return []
        nums.sort()
        result = []
        for i in range(0, len(nums) - 3):
            # incase index is zero, the nums[index - 1] will return the last number in the list, so make sure the index is not 0
            if i and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                #######most important! line ########
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                want = target - nums[i] - nums[j]
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    sums = nums[left] + nums[right]
                    if sums == want:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif sums < want:
                        left += 1
                    else:
                        right -= 1
        return result