class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # in-place
        # 0:dead, 3:live->dead
        # 1:live, 2:dead->live
        
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                neighbor_live = self.count_neighbor_live(board, m, n, i, j)
                if board[i][j]==1 and (neighbor_live < 2 or neighbor_live > 3): 
                    # live -> dead caused by under-population or over-population
                    board[i][j]=3
                if board[i][j]==0 and neighbor_live == 3:
                    # dead->live because of reproduction
                    board[i][j]=2
        for i in range(m):
            for j in range(n):
                if board[i][j] == 3:
                    board[i][j] = 0
                if board[i][j] == 2:
                    board[i][j] = 1
        
        
    def count_neighbor_live(self, board, m, n, i, j):
        num_of_live = 0
        if i>0 and j>0: # NW 
            num_of_live += board[i-1][j-1]%2
        if i>0: # NN
            num_of_live += board[i-1][j]%2
        if i>0 and j<n-1:  # NE
            num_of_live += board[i-1][j+1]%2
        
        if j>0: # WW 
            num_of_live += board[i][j-1]%2
        if j<n-1:  # EE
            num_of_live += board[i][j+1]%2
        
        if i<m-1 and j>0: # SW
            num_of_live += board[i+1][j-1]%2
        if i<m-1: # SS
            num_of_live += board[i+1][j]%2
        if i<m-1 and j<n-1:  # SE
            num_of_live += board[i+1][j+1]%2
        return num_of_live
    
# print Solution().gameOfLife([[0,0,0], [0,0,1], [0,1,1]])
print Solution().gameOfLife([[0,0,0,0,0],
                             [0,0,1,0,0],
                             [0,0,1,0,0],
                             [0,0,1,0,0],
                             [0,0,0,0,0]])
# [[0,0,0,0,0],[0,0,0,0,0],[0,1,1,1,0],[0,0,0,0,0],[0,0,0,0,0]]