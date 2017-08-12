class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        result = "1"

        if n <= 1:
            return result
        while n > 1:
            result = self.count(result)
            n -= 1
        return result

    def count(self, string):
        curr = "#"
        cot = 0
        res = ""
        for s in string:
            if s != curr:
                if curr != "#":
                    res = res + str(cot) + curr
                cot = 1
                curr = s
            else:
                cot += 1

        res = res + str(cot) + s
        return res