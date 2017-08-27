class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if word == "":
            return True
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        if n == 0:
            return False
        visited = [[False for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if self.checkNeighber(board, word, visited, i, j):
                    return True
        return False

    def checkNeighber(self, board, word, visited, row, col):
        if word == "":
            return True
        m, n = len(board), len(board[0])
        if row < 0 or col < 0 or row > m - 1 or col > n - 1:
            return False
        if board[row][col] == word[0] and not visited[row][col]:
            visited[row][col] = True
            if self.checkNeighber(board, word[1:], visited, row + 1, col) or self.checkNeighber(board, word[1:],
                                                                                                visited, row - 1,
                                                                                                col) or self.checkNeighber(
                    board, word[1:], visited, row, col + 1) or self.checkNeighber(board, word[1:], visited, row,
                                                                                  col - 1):
                return True
            else:
                visited[row][col] = False