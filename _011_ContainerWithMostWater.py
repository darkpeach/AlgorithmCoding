# simple solution but excess time limit
# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         maximum = 0
#         for i in range(len(height)):
#             for j in range(i, len(height)):
#                 width = j - i
#                 area = min(height[i], height[j]) * width
#                 maximum = max(maximum, area)
#         return maximum
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        left = 0
        right = len(height) - 1
        while left < right:
            maxArea = max(maxArea, min(height[left], height[right]) * (right-left))
            if height[left] <= height[right]:
                left += 1
            else :
                right -= 1
        return maxArea