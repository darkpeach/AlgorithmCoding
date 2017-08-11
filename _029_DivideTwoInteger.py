class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        int_max = (1 << 31) - 1
        if divisor == 0:
            return int_max
        neg = dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0
        dividend, divisor = abs(dividend), abs(divisor)
        result, shift = 0, 31
        while shift >= 0:
            if dividend >= divisor << shift:
                dividend -= divisor << shift
                result += 1 << shift
            shift -= 1
        if neg:
            result = -result
        if result > int_max:
            return int_max
        ans = [result, dividend]
        return ans
