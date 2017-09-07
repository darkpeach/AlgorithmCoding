class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def dfs(s, sub, partitionList, result):
            if sub == 4:
                if s == "":
                    result.append(partitionList[1:])
                    return
            else:
                for i in range(1, 4):
                    if i <= len(s):
                        if int(s[:i]) <= 255:
                            dfs(s[i:], sub + 1, partitionList + "." + s[:i], result)
                        if s[0] == "0":
                            break

        result = []
        dfs(s, 0, "", result)
        return result