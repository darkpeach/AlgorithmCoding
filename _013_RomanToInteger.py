class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        Roman = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        if s == "":
            return 0
        start = len(s)-1
        sum = Roman[s[start]]
        while start - 1 >= 0:
            if Roman[s[start - 1]] >= Roman[s[start]]:
                sum += Roman[s[start-1]]
            else:
                sum -= Roman[s[start-1]]
            start -= 1
        return sum