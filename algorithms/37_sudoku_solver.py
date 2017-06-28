class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0:
            return []
        self.board = [[int(j) if j != '.' else j for j in list(i)] for i in board]
        self.solve()
        for i in range(9):
            for j in range(9):
                board[i][j] = str(self.board[i][j])
        
    def solve(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == '.':
                    for k in range(1, 10):
                        if self.isValidCell(i, j, k):
                            self.board[i][j] = k
                            if self.solve():
                                return True
                            else:
                                self.board[i][j] = '.'
                    # has empty cell in this run, need to check. 
                    return False
        return True

    def isValidCell(self, i, j, k):
        # Check row
        for t in range(9):
            if t != j and self.board[i][t] == k:
                return False
        # Check col
        for t in range(9):
            if i != t and self.board[t][j] == k:
                return False
        # Check square:
        bi, bj = i / 3 * 3, j / 3 * 3
        for u in range(bi, bi + 3):
            for v in range(bj, bj + 3):
                if u != i and v != j and self.board[u][v] == k:
                    return False
        return True

print Solution().solveSudoku(
    ["..9748...", "7........", ".2.1.9...", "..7...24.", ".64.1.59.",
     ".98...3..", "...8.3.2.", "........6", "...2759.."])
# ["519748632","783652419","426139875","357986241","264317598","198524367",
# "975863124","832491756","641275983"]
