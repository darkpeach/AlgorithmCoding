class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        redPtr = 0
        bluePtr = len(nums) - 1
        index = 0
        while index <= bluePtr:
            print("index is %d", index)
            if nums[index] == 2 and index != bluePtr:
                while nums[bluePtr] == 2 and index < bluePtr:
                    bluePtr -= 1
                nums[index], nums[bluePtr] = nums[bluePtr], nums[index]
                bluePtr -= 1
                print(bluePtr)
            if nums[index] == 0:
                nums[index], nums[redPtr] = nums[redPtr], nums[index]
                redPtr += 1
                print(redPtr)
            index += 1
            print(nums)
