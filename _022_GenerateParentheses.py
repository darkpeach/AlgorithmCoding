class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def dfs(l, r, string, result):
            if r < l:
                return
            if l == 0 and r == 0:
                result.append(string)
            if r > 0:
                dfs(l, r - 1, string + ")", result)
            if l > 0:
                dfs(l - 1, r, string + "(", result)

        if not n:
            return []
        else:
            result = []
            dfs(n, n, "", result)

        return result