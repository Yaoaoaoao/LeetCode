class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        board = [list(i) for i in board]
        result = []
        for word in words:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if self.dfs(board, i, j, word):
                        result.append(word)
        return list(set(result))
        
    def dfs(self, board, i, j, word):
        if board[i][j] == word[0]:
            pick = word[0]
            word = word[1:]
            if not word:
                return True
            board[i][j] = ''
            if i > 0 and self.dfs(board, i-1, j, word):
                board[i][j] = pick
                return True
            if j > 0 and self.dfs(board, i, j-1, word):
                board[i][j] = pick
                return True
            if i < len(board)-1 and self.dfs(board, i+1, j, word):
                board[i][j] = pick
                return True
            if j < len(board[0])-1 and self.dfs(board, i, j+1, word):
                board[i][j] = pick
                return True
            board[i][j] = pick
        else:
            return False
    
print Solution().findWords(["ab","cd"], ["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"]) #["ab","ac","bd","ca","db"]