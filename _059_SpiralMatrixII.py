class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        ept = [0] * n
        for index in range(n):
            result.append(copy.copy(ept))
        if n == 0:
            return []
        if n == 1:
            return [[1]]
        up = 0
        left = 0
        down = n - 1
        right = n - 1
        count = 1
        direction = 0
        while True:
            if direction == 0:
                for i in range(left, right + 1):
                    print(count)
                    result[up][i] = count
                    count += 1
                up += 1
            if direction == 1:
                for j in range(up, down + 1):
                    print(count,direction)
                    result[j][right] = count
                    count += 1
                right -= 1
            if direction == 2:
                for k in range(right, left -1, -1):
                    print(count)
                    result[down][k] = count
                    count += 1
                down -= 1
            if direction == 3:
                for p in range(down, up - 1, -1):
                    result[p][left] = count
                    count += 1
                left += 1
            direction += 1
            direction %= 4
            if count == n * n + 1:
                return result