class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if wordDict == []:
            if s == '':
                return True
            else:
                return False
        mapList = [False for i in range(len(s)+1)]
        mapList[0] = True
        maxLength = max(len(item) for item in wordDict)
        for i in range(1,len(s) + 1):
            for j in range(1, min(i, maxLength) + 1):
                if mapList[i - j] == False:
                    continue
                if s[i-j:i] in wordDict:
                    mapList[i] = True
                    break
        return mapList[len(s)]   