class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        """
        In the first sweep, we visit each entry in natural order and 
        answer[i][j] = min(Integer.MAX_VALUE, min(answer[i - 1][j], answer[
        i][j - 1]) + 1).
        In the second sweep, we visit each entry in reverse order and 
        answer[i][j] = min(answer[i][j], min(answer[i + 1][j], answer[i][j + 
        1]) + 1).
        """
        import sys
        m, n = len(matrix), len(matrix[0])
        distance = [[0 if matrix[i][j] == 0 else sys.maxint
                     for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                left = distance[i][j - 1] if j > 0 else sys.maxint
                top = distance[i - 1][j] if i > 0 else sys.maxint
                distance[i][j] = min(distance[i][j], min(left, top) + 1)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                right = distance[i][j + 1] if j < n - 1 else sys.maxint
                bottom = distance[i + 1][j] if i < m - 1 else sys.maxint
                distance[i][j] = min(distance[i][j], min(right, bottom) + 1)
        return distance


print Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]])
