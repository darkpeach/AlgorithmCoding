class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        mp = {}
        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if row == 1 or col == 1:
                    mp[(row, col)] = 1
                else:
                    mp[(row, col)] = mp[(row - 1, col)] + mp[(row, col - 1)]

        return mp[(m, n)]