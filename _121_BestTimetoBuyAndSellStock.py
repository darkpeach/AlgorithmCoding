class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low = (1 << 31) - 1
        total = 0
        for price in prices:
            if price - low > total:
                total = price - low
            if price < low:
                low = price
        return total