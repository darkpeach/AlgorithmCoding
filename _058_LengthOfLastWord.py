class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        result = s.strip().split(" ")[-1]
        return len(result)
