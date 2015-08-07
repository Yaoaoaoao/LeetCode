class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        spiral = []
        while matrix:
            spiral.extend(matrix.pop(0))
            if matrix and matrix[0]: # empty list
                for i in matrix:
                    spiral.append(i.pop(-1))
            if matrix:
                spiral.extend(matrix.pop(-1)[::-1])
            if matrix and matrix[0]: # empty list
                col = []
                for i in matrix:
                    col.append(i.pop(0))
                spiral.extend(col[::-1])
        return spiral

    
print Solution().spiralOrder([
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]) # [1,2,3,6,9,8,7,4,5]
print Solution().spiralOrder([[7],[9],[6]])
print Solution().spiralOrder([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])