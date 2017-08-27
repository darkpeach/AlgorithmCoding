class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool

        """
        if not matrix or matrix == [[]]:
            return False
        row = len(matrix)
        col = len(matrix[0])
        start, end = 0, row - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                start = mid
            else:
                end = mid
        if matrix[end][0] == target:
            return True
        elif matrix[end][0] < target:
            r = end
        else:
            r = start
        start, end = 0, col - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if matrix[r][mid] == target:
                return True
            elif matrix[r][mid] < target:
                start = mid
            else:
                end = mid
        if matrix[r][start] == target or matrix[r][end] == target:
            return True
        return False