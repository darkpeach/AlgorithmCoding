# pure dfs
# class Solution(object):
#     def combine(self, n, k):
#         """
#         :type n: int
#         :type k: int
#         :rtype: List[List[int]]
#         """
#         def dfs(bag, partitionList, index, result):
#             if len(partitionList) == k:
#                 result.append(partitionList)
#             else:
#                 for i in range(index + 1, len(bag)):
#                     dfs(bag, partitionList + [bag[i]], i, result)
#         nList = []
#         for i in range(n):
#             nList.append(i + 1)
#         result = []
#         dfs(nList, [], -1, result)
#         return result



class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.dfs([], -1, n, k)
        return self.result
    def dfs(self, partitionList, index, n, k):
        if len(partitionList) == k:
            self.result.append(partitionList)
        else:
            for i in range(index + 1, n):
                self.dfs(partitionList + [i+1], i, n, k)