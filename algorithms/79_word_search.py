class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        #dfs stack
        board = [list(i) for i in board]
        rows, cols = len(board), len(board[0])
        for r in range(rows):
            for c in range(cols):
                if self.dfs(board, r, c, word):
                    return True
        return False
                
    def dfs(self, board, i, j, word):
        if board[i][j] == word[0]:
            tmp = word[0]
            word = word[1:]
            if not word:
                return True
            board[i][j] = '' # explored
            if i>0 and self.dfs(board, i-1, j, word):
                return True
            if i<len(board)-1 and self.dfs(board, i+1, j, word):
                return True
            if j>0 and self.dfs(board, i, j-1, word):
                return True
            if j<len(board[0])-1 and self.dfs(board, i, j+1, word):
                return True
            board[i][j] = tmp
            return False
        else:
            return False
    
    
print Solution().exist(["aa"], "aa") #true
print Solution().exist(["ab","cd"], "aa") #false
print Solution().exist(["ab","cd"], "abcd") #false
print Solution().exist(["ABCE", "SFCS", "ADEE"], "ABCCED") #true
print Solution().exist(["ABCE", "SFCS", "ADEE"], "SEE") #true
print Solution().exist(["ABCE", "SFCS", "ADEE"], "ABCB") #false
