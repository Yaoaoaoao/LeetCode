class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # O(1) 176ms
        rows, cols = len(matrix), len(matrix[0])
        col0 = False # reverse the row assign action to save rows
        # mark the state at first row and col  
        for i in range(0, rows):
            if matrix[i][0] == 0:
                col0 = True
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        # mark the entire row or column to 0 
        for i in reversed(range(rows)):
            for j in reversed(range(1, cols)):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0: 
                matrix[i][0] = 0
        
        # # O(m+n) 216ms
        # m, n = [], []
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])):
        #         if matrix[i][j] == 0:
        #             m.append(i)
        #             n.append(j)
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])):
        #         if i in m or j in n:
        #             matrix[i][j] = 0
        return matrix
                
print Solution().setZeroes([[1,2,3,4,5], [6,0,8,9,10], [11,12,13,14,15], [16,17,18,0,20], [21,22,23,24,25]])