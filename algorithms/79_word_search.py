class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        board = [list(i) for i in board]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False
        
    def dfs(self, board, i, j, word):
        if board[i][j] == word[0]:
            pick = word[0]
            word = word[1:]
            if not word:
                return True
            board[i][j] = ''
            if i > 0 and self.dfs(board, i-1, j, word):
                return True
            if j > 0 and self.dfs(board, i, j-1, word):
                return True
            if i < len(board)-1 and self.dfs(board, i+1, j, word):
                return True
            if j < len(board[0])-1 and self.dfs(board, i, j+1, word):
                return True
            board[i][j] = pick
            return False
        else:
            return False
    
    
print Solution().exist(["a"], "a") #true
print Solution().exist(["aa"], "aa") #true
print Solution().exist(["ab","cd"], "aa") #false
print Solution().exist(["ab","cd"], "abcd") #false
print Solution().exist(["ABCE", "SFCS", "ADEE"], "ABCCED") #true
print Solution().exist(["ABCE", "SFCS", "ADEE"], "SEE") #true
print Solution().exist(["ABCE", "SFCS", "ADEE"], "ABCB") #false
