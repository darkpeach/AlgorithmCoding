class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lastShown = {}
        result = 0
        left = 0
        for i in range(len(s)):
            if s[i] in lastShown and lastShown[s[i]] >= left :
                left = lastShown[s[i]] + 1
            lastShown[s[i]] = i
            result = max(result,i-left+1)
        return result