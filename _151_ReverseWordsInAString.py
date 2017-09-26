class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        List = s.split()
        print(List)
        result = []
        for i in range(len(List) - 1, -1, -1):
            print(i)
            result.append(List[i])
        return " ".join(result)
