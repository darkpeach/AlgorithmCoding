class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dictionary = {}
        for word in strs:
            sortedword = "".join(sorted(word))
            if sortedword in dictionary:
                dictionary[sortedword].append(word)
            else:
                dictionary[sortedword] = [word]
        result = []
        for item in dictionary:
            result.append(dictionary[item])
        return result
