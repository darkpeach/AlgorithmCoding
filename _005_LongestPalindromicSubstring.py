class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        maxlength = 0
        ansl = 0
        ansr = 0
        for i in range(0,len(s)):
            left, right, length = self.getPalindrome(s,i,i)
            if length > maxlength:
                maxlength = length
                ansl = left
                ansr = right
            left, right, length = self.getPalindrome(s,i,i+1)
            if length > maxlength:
                maxlength = length
                ansl = left
                ansr = right
        return s[ansl: ansr+1]
    def getPalindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left+1, right-1, right - left -1