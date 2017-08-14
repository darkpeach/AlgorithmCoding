class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Non-recursive solution
        if not nums:
            return []
        stack = [-1]
        permutation = []
        permutations = []
        while len(stack):
            index = stack.pop()
            index += 1
            while index < len(nums):
                if nums[index] not in permutation:
                    break
                index += 1
            else:
                if len(permutation):
                    permutation.pop()
                continue

            stack.append(index)
            stack.append(-1)
            permutation.append(nums[index])
            if len(permutation) == len(nums):
                permutations.append(list(permutation))

        return permutations


# recursive solution
#         def dfs(bag,partitionList,result):
#             if bag == []:
#                 result.append(partitionList)
#             else:
#                 for i in range(len(bag)):
#                     dfs(bag[:i] + bag[i+1:], partitionList + [bag[i]], result)

#         if not nums:
#             return []
#         result = []
#         dfs(nums,[],result)
#         return result
