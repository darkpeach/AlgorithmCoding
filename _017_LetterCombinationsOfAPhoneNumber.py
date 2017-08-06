#Backtracking solution
# class Solution(object):
#     def letterCombinations(self, digits):
#         """
#         :type digits: str
#         :rtype: List[str]
#         """
#         if not len(digits):
#             return []
#         charsArray = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
#         res = []
#         for digit in digits:
#             chars = charsArray[int(digit)]
#             temp = []
#             for char in chars:
#                 if len(res):
#                     for item in res:
#                         temp.append(item + char)
#                 else:
#                     temp.append(char)
#             res = copy.copy(temp)
#
#         return res
#

#DFS solution
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []

        def dfs(index, string, result):
            if index == len(digits):
                result.append(string)
            else:
                for char in charsArray[int(digits[index])]:
                    dfs(index + 1, string + char, result)

        charsArray = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        if not len(digits):
            return []
        dfs(0, "", result)
        return result