class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        example = strs[0]
        for i in range(len(example)):
            for str in strs:
                if len(str) <= i or example[i] != str[i]:
                    print(i)
                    return example[0:i]
        return example


