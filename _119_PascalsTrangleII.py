class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1]
        while rowIndex >= 1:
            tempList = []
            for i in range(len(result) + 1):
                if i == 0:
                    tempList.append(1)
                elif i == len(result):
                    tempList.append(1)
                else:
                    tempList.append(result[i] + result[i - 1])
            result = tempList
            rowIndex -= 1
        return result