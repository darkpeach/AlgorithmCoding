class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        left = 0
        up = 0
        right =len(matrix[0])
        down = len(matrix)
        direction = 0
        res = []
        while True:
            if direction == 0:
                for i in range(left, right):
                    print(up,i)
                    res.append(matrix[up][i])
                up += 1
            if direction == 1:
                for j in range(up, down):
                    print(j,right - 1)
                    res.append(matrix[j][right - 1])
                right -= 1
            if direction == 2:
                for k in range(right-1, left-1, -1):
                    res.append(matrix[down - 1][k])
                down -= 1
            if direction == 3:
                for l in range(down -1, up -1, -1):
                    res.append(matrix[l][left])
                left += 1
            direction += 1
            direction %= 4
            if up > down-1 or left > right -1 :
                return res