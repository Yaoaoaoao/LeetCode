class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        # DP solution (highest vote)
        if len(matrix)==0:
            return 0
        w, h = len(matrix[0]), len(matrix)
        max_ = 0
        square = [[None for i in range(w)] for j in range(h)]
        # i = 0
        for j in range(w):
            square[0][j] = int(matrix[0][j])
            max_ = max(max_, square[0][j])
        # j = 0
        for i in range(h):
            square[i][0] = int(matrix[i][0])
            max_ = max(max_, square[i][0])
        # i>0 and j>0
        for i in range(1,h):
            for j in range(1, w):
                if matrix[i][j] == '0':
                    square[i][j] = 0
                else:
                    square[i][j] = min(square[i-1][j-1], square[i-1][j], square[i][j-1])+1
                    max_ = max(max_, square[i][j])
        return max_**2
    
# print Solution().maximalSquare([])
# print Solution().maximalSquare(["0"])
print Solution().maximalSquare(["1"])
# print Solution().maximalSquare(["00","00"])