class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        int_max = (1 << 31) - 1
        int_min = -(1 << 31)
        str = str.strip()
        start = 0
        flag = 1
        if str == "" or str == None:
            return 0
        if str[start] == "-":
            flag = -1
            start += 1
        elif str[start] == "+":
            start += 1

        result = 0
        for i in range(start, len(str)):
            if str[i].isdigit():
                result = result * 10 + int(str[i])
            else:
                break
        result = result * flag
        if result > int_max:
            result = int_max
        elif result < int_min:
            result = int_min
        return result
