class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        col_1 = 1
        col = len(matrix[0])
        row = len(matrix)
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    if c == 0:
                        col_1 = 0
                    else:
                        matrix[0][c] = 0

        for r in range(row - 1, -1, -1):
            for c in range(col - 1, 0, -1):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        if col_1 == 0:
            for i in range(row):
                matrix[i][0] = 0
