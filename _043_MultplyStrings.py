class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = [0] * (len(num1) + len(num2))
        ptr = len(result) - 1
        for n1 in reversed(num1):
            pos = ptr
            for n2 in reversed(num2):
                result[pos] += int(n1) * int(n2)
                result[pos - 1] += result[pos] // 10
                result[pos] %= 10
                pos -= 1
            ptr -= 1

        i = 0
        while i < len(result) and result[i] == 0:
            i += 1
        return "".join(map(str, result[i:] or [0]))