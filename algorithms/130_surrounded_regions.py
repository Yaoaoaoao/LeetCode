class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0: 
            board_ = [list(i) for i in board]
            m, n = len(board_), len(board_[0])
            islands = []
            for i in range(m):
                for j in range(n):
                    if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and board_[i][
                        j] == 'O':
                        islands.append((i, j))
            while len(islands) > 0:
                i, j = islands.pop(0)
                if 0 <= i < m and 0 <= j < n and board_[i][j] == 'O':
                    board_[i][j] = 'V'
                    islands.append((i - 1, j))
                    islands.append((i + 1, j))
                    islands.append((i, j - 1))
                    islands.append((i, j + 1))
                    
            for i in range(m):
                for j in range(n):
                    if board_[i][j] == 'O':
                        board_[i][j] = 'X'
                    elif board_[i][j] == 'V':
                        board_[i][j] = 'O'
            
            for i in range(m):
                board[i] = ''.join(board_[i])
    

Solution().solve(["XXXX", "XOOX", "XXOX", "XOXX"])
