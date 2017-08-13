# Recursive dfs
# class Solution(object):
#     def permute(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#
#         def dfs(bag, partitionList, result):
#             if bag == []:
#                 result.append(partitionList)
#             else:
#                 for i in range(len(bag)):
#                     dfs(bag[:i] + bag[i + 1:], partitionList + [bag[i]], result)
#
#         if not nums:
#             return []
#         result = []
#         dfs(nums, [], result)
#         return result


#Non-recursive solution