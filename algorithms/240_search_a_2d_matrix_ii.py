class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not target:
            return False
        # start from the top right corner
        row, col = len(matrix), len(matrix[0])
        r,c = 0, col-1
        while 0 <= r < row and 0 <= c < col:
            if target == matrix[r][c]:
                return True
            elif target < matrix[r][c]:
                c -= 1
            elif target > matrix[r][c]:
                r += 1
        else:
            return False
    

print Solution().searchMatrix([
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
], 20)