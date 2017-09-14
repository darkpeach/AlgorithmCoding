class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if triangle == []:
            return 0
        if len(triangle) == 1:
            return min(triangle[0])
        for i in range(1, len(triangle)):
            length = len(triangle[i])
            triangle[i][0] += triangle[i - 1][0]
            triangle[i][length - 1] += triangle[i - 1][length - 2]
            for k in range(1, length - 1):
                triangle[i][k] += min(triangle[i - 1][k], triangle[i - 1][k - 1])

        return min(triangle[-1])
