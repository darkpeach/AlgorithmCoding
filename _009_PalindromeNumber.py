class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or x <= -(1<<31):
            return False;
        if x == self.postiveReverse(x):
            return True
        else:
            return False
    def postiveReverse(self, num):
        result = 0
        while num > 9:
            residual =num % 10
            result = (result + residual) * 10
            num = num // 10
        result = result +num
        return result