class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        if matrix:
            cols = len(matrix[0])
        for r in range(rows):
            for c in range(cols - r - 1):
                print(r, c)
                print(cols - r - 1, rows - c - 1)
                matrix[r][c], matrix[cols - c - 1][rows - r - 1] = matrix[cols - c - 1][rows - r - 1], matrix[r][c]
        matrix.reverse()

