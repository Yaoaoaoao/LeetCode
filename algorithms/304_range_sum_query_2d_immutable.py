class NumMatrix(object):
    # O(nm) space, O(nm) initial, O(1) query
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if matrix is None or not matrix:
            return
        n, m = len(matrix), len(matrix[0])
        self.subset_sum = [[0 for j in range(m+1)] for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                self.subset_sum[i][j] = matrix[i-1][j-1] + self.subset_sum[i-1][j] + self.subset_sum[i][j-1]  - self.subset_sum[i-1][j-1]


    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.subset_sum[row2+1][col2+1] - self.subset_sum[row2+1][col1] - self.subset_sum[row1][col2+1] + self.subset_sum[row1][col1]



# Your NumMatrix object will be instantiated and called as such:
matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]
numMatrix = NumMatrix(matrix)
print numMatrix.sumRegion(2, 1, 4, 3) #-> 8
print numMatrix.sumRegion(1, 1, 2, 2) #-> 11
print numMatrix.sumRegion(1, 2, 2, 4) #-> 12