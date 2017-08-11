class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        start, end = 0, len(nums) - 1
        # position the leftbound into a three element range
        while start+1 < end:
            mid  = ( start + end ) // 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        # find the leftbound
        if nums[start] == target:
            leftbound = start
        elif nums[end] == target:
            leftbound = end
        else:
            return [-1, -1]
        # position the rightbound into a three element range
        start, end = leftbound, len(nums) - 1
        while start+1 < end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid
        # find the rightbound
        if nums[end] == target:
            rightbound = end
        else:
            rightbound = start
        return [leftbound, rightbound]