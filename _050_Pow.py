class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 1:
            return x
        if n == 0:
            return 1
        isNegative = 0
        if n < 0:
            isNegative = 1
            n *= -1

        left = n // 2
        right = n % 2
        t1 = self.myPow(x, left)
        t2 = self.myPow(x, right)
        if isNegative:
            return 1 / (t1 * t1 * t2)
        else:
            return t1 * t1 * t2
