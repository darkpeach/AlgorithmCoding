class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        result = [1,2]
        for i in range(n - 2):
            result.append(result[-1] + result[-2])
        return result[-1]