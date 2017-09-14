class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def fill(x, y):
            if x < 0 or x > m - 1 or y < 0 or y > n - 1 or board[x][y] != "O":
                return
            else:
                queue.append((x, y))
                board[x][y] = "T"
                return

        def bfs(x, y):
            if board[x][y] == "O":
                queue.append((x, y))
                fill(x, y)
            while queue:
                cord = queue.pop()
                l, k = cord[0], cord[1]
                fill(l - 1, k)
                fill(l + 1, k)
                fill(l, k - 1)
                fill(l, k + 1)

        if len(board) == 0:
            return
        m, n = len(board), len(board[0])
        queue = []

        for i in range(n):
            bfs(0, i)
            bfs(m - 1, i)
        for j in range(m):
            bfs(j, 0)
            bfs(j, n - 1)

        for p in range(m):
            for q in range(n):
                if board[p][q] == "T":
                    board[p][q] = "O"
                else:
                    board[p][q] = "X"
        return