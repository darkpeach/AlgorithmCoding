class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1
        if x < 0:
            flag = -1
            x = -x


        result = 0

        while x > 9:
            residual = x % 10
            result = (result + residual) * 10
            x = x//10
        result = result + x % 10

        result = result * flag
        if result < -(1<<31) or result > (1<<31) - 1:
            result = 0
        return result