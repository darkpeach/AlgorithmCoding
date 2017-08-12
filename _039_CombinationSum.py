class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(sums, index, partitionList, result):
            print(index)
            print(sums)
            print(partitionList)
            if sums  == target:
                result.append(partitionList)
            elif sums < target:
                for i in range(index, len(candidates)):
                    if sums + candidates[i] > target:
                        return
                    dfs(sums + candidates[i], i, partitionList + [candidates[i]], result)
            else:
                return
        if len(candidates) == 0:
            return []
        candidates.sort()
        result = []
        dfs(0, 0, [], result)
        return result