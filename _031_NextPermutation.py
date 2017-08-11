class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # check if the list has already been fully permutated
        for findIndex in range(len(nums) - 2, -1, -1):
            if nums[findIndex] < nums[findIndex + 1]:
                # jump out if there is the first element that smaller than its next neighber
                break
        else:
            nums.reverse()
            return

        # find the element that just larger than the first element
        for swapIndex in range(len(nums) - 1, findIndex, -1):
            if nums[swapIndex] > nums[findIndex]:
                # swap these two number
                nums[findIndex], nums[swapIndex] = nums[swapIndex], nums[findIndex]
                break

        # reverse the rest list on findIndex's right-side (in Place)
        temp = nums[findIndex + 1:]
        temp.reverse()
        nums[findIndex + 1:] = temp
        return