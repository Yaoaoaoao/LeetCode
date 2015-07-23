class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        # one-line python solution
        # matrix[:] = zip(*matrix[::-1])

        # one space solution
        n = len(matrix)
        for i in range(int(n / 2) + 1):
            for j in range(i, n - 1 - i):
                matrix[i][j], matrix[n - 1 - j][i], matrix[n - 1 - i][n - 1 - j], matrix[j][n - 1 - i] = \
                    matrix[n - 1 - j][i], matrix[n - 1 - i][n - 1 - j], matrix[j][n - 1 - i], matrix[i][j]

        return matrix[:]
        
# print Solution().rotate([[1,2],[3,4]])
print Solution().rotate([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])