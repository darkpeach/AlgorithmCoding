class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        preList = self.grayCode(n - 1)
        result = preList
        for item in reversed(preList):
            result.append(1 << (n - 1) | item)
        return result

