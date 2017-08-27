class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len_1 = len(word1)
        len_2 = len(word2)
        dp = [[0] * (len_1 + 1) for i in range(len_2 + 1)]
        for i in range(len_1 + 1):
        #deleting
            dp[0][i] = i
        for j in range(len_2 + 1):
        #inserting
            dp[j][0] = j
        for i in range(1, len_1 + 1):
            for j in range(1, len_2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[j][i] = dp[j - 1][i - 1]
                else:
                    dp[j][i] = min(dp[j - 1][i - 1], dp[j][i - 1], dp[j - 1][i]) + 1
        return dp[len_2][len_1]