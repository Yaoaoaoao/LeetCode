class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        M = 1000000000 + 7
        dp = [[0 for __ in range(n)] for _ in range(m)]
        dp[i][j] = 1
        count = 0
        for move in range(N):
            temp = [[0 for __ in range(n)] for _ in range(m)]
            for x in range(m):
                for y in range(n):
                    if x == m - 1:
                        count = (count + dp[x][y]) % M
                    if y == n - 1:
                        count = (count + dp[x][y]) % M
                    if x == 0:
                        count = (count + dp[x][y]) % M
                    if y == 0:
                        count = (count + dp[x][y]) % M

                    sum_ = 0
                    sum_ += dp[x - 1][y] if x > 0 else 0
                    sum_ += dp[x + 1][y] if x < m - 1 else 0
                    sum_ += dp[x][y - 1] if y > 0 else 0
                    sum_ += dp[x][y + 1] if y < n - 1 else 0
                    temp[x][y] = sum_ % M
            dp = temp
        return count


print Solution().findPaths(1, 3, 3, 0, 1)
