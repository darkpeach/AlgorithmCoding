class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        digits[0] += 1
        i = 0
        carry = 0
        while i < len(digits):
            sum = digits[i] + carry
            digits[i] = sum % 10
            carry = sum // 10
            i += 1
        if carry > 0:
            digits.append(1)
        digits.reverse()
        return digits