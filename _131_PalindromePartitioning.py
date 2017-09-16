class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.result = []
        if len(s) == 0:
            return []
        self.dfs(s, [])
        return self.result

    def checkPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True

    def dfs(self, s, stringList):
        if len(s) == 0:
            self.result.append(stringList)
            return
        for i in range(len(s)):
            if self.checkPalindrome(s[:i + 1]):
                self.dfs(s[i + 1:], stringList + [s[:i + 1]])
        return
