class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        high, low = (1<<31) - 1, (1<<31) - 1
        total = 0
        for price in prices:
            if price > high:
                high = price
            else:
                total += high - low
                low, high = price, price
        return total + high - low