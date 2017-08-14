class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(bag, partitionList, result):
            print(partitionList)
            if len(partitionList) == len(nums):
                result.append(list(partitionList))
            else:
                for i in range(len(bag)):
                    if bag[i] == bag[i-1] and i != 0:
                        continue
                    dfs(bag[:i] + bag[i+1:], partitionList + [bag[i]], result)
        if not nums:
            return []
        nums.sort()
        result = []
        dfs(nums, [], result)
        return result