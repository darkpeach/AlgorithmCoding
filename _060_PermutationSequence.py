class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        restList = range(1, n + 1)
        result = []
        for i in range(n):
            factor = math.factorial(n - i - 1)
            rangeForDigit = k // factor
            remain = k % factor
            if remain == 0:
                rangeForDigit -= 1
                remain = remain + factor
            k = remain
            digit = restList[rangeForDigit]
            result.append(digit)
            restList.remove(digit)
        return "".join(map(str, result))
