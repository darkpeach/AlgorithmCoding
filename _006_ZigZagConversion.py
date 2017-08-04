class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows > len(s):
            return s

        ptr = 1
        index = 0
        resultList = [""] * numRows
        for x in s:
            resultList[index] += x
            if index == 0:
                ptr = 1
            elif index == numRows - 1:
                ptr = -1
            index += ptr

        return "".join(resultList)