class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        # row
        for i in board:
            if not self.valid(i):
                return False
        # column
        for i in zip(*board):
            if not self.valid(i):
                return False
        # sub-box
        for i in xrange(0,9,3):
            for j in xrange(0,9,3):
                if not self.valid([board[x][y] for x in range(i, i+3) for y in range(j, j+3)]):
                    return False
        return True
    
    def valid(self, l):
        d = {}
        for i in l:
            if i == ".": 
                continue
            if i in d:
                return False
            else:
                d[i] = True
        else:
            return True