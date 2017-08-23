class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = list(a)
        a.reverse()
        b = list(b)
        b.reverse()
        result = []

        i = 0
        carry = 0
        while i < max(len(a), len(b)):
            if i < len(a):
                digit_a = int(a[i])
            else:
                digit_a = 0
            if i < len(b):
                digit_b = int(b[i])
            else:
                digit_b = 0
            sum = digit_a + digit_b + carry
            result.append(sum % 2)
            carry = sum // 2
            i += 1
        if carry > 0:
            result.append(1)
        result.reverse()
        return "".join(map(str, result))