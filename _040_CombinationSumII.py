class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(sums, index, partitionList, result):

            if sums == target:
                result.append(partitionList)
            elif sums < target:
                for i in range(index + 1, len(candidates)):
                    if sums + candidates[i] > target or (candidates[i] == candidates[i-1] and i != index + 1):
                        continue
                    dfs(sums + candidates[i], i, partitionList + [candidates[i]], result)
            else:
                return
        if len(candidates) == 0:
            return []
        candidates.sort()
        result = []
        dfs(0,-1,[],result)
        return result