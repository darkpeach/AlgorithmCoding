class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        mp = {}
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if obstacleGrid[m - row][n - col] == 1:
                    mp[(row, col)] = 0
                elif row == 1 and col == 1:
                    mp[(row, col)] = 1
                elif (row == 1 and mp[(row, col - 1)] == 1) or (col == 1 and mp[(row - 1, col)] == 1):
                    mp[(row, col)] = 1
                elif (row == 1 and mp[(row, col - 1)] == 0) or (col == 1 and mp[(row - 1, col)] == 0):
                    mp[(row, col)] = 0
                else:
                    mp[(row, col)] = mp[(row, col - 1)] + mp[(row - 1, col)]
        return mp[(m, n)]
