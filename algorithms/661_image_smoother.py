class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        m, n = len(M), len(M[0])
        for i in range(m):
            row = []
            for j in range(n):
                sum_ = []
                if i > 0:
                    if j > 0: sum_.append(M[i - 1][j - 1])
                    sum_.append(M[i - 1][j])
                    if j < n - 1: sum_.append(M[i - 1][j + 1])

                if j > 0: sum_.append(M[i][j - 1])
                sum_.append(M[i][j])
                if j < n - 1: sum_.append(M[i][j + 1])

                if i < m - 1:
                    if j > 0: sum_.append(M[i + 1][j - 1])
                    sum_.append(M[i + 1][j])
                    if j < n - 1: sum_.append(M[i + 1][j + 1])

                row.append(sum(sum_) / len(sum_))
            result.append(row)
        return result


print Solution().imageSmoother(
    [[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13], [14, 15, 16]])
