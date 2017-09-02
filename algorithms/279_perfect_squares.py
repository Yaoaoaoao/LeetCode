class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        sq = [i * i for i in range(1, int(n ** 0.5) + 1)]
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = i
            for s in sq:
                if s > i: break
                dp[i] = min(dp[i], dp[i - s] + 1)
        return dp[-1]


print Solution().numSquares(9)
print Solution().numSquares(12)
print Solution().numSquares(13)
print Solution().numSquares(26)
