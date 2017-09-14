class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(e for e in s if e.isalnum())
        s = s.upper()
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True
