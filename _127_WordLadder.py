import collections
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList)
        wordLen = len(beginWord)
        queue = collections.deque([(beginWord, 1)])
        while queue:
            currWord, currLen = queue.popleft()
            if currWord == endWord:
                return currLen
            for i in range(wordLen):
                part1 = currWord[:i]
                part2 = currWord[i + 1:]
                for j in "abcdefghijklmnopqrstuvwxyz":
                    newWord = part1 + j + part2
                    if newWord in wordSet:
                        queue.append((newWord, currLen + 1))
                        wordSet.remove(newWord)
        return 0