class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        result = [[1]]
        while numRows > 1:
            workList = result[-1]
            tempList = []
            for i in range(len(workList) + 1):
                if i == 0:
                    tempList.append(1)
                elif i == len(workList):
                    tempList.append(1)
                else:
                    tempList.append(workList[i] + workList[i - 1])
            result.append(tempList)
            numRows -= 1
        return result