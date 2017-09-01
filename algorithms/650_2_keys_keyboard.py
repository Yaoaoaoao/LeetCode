class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        # O(n**2)
        if n <= 1:
            return 0
        dp = range(n + 1)
        dp[0] = dp[1] = 0
        for i in range(2, n + 1):
            # dp[i] = dp[1] + 1 + (i - 1) copy and paste i-1 times
            # dp[i] = i
            for j in range(2, i / 2 + 1):
                if i % j == 0:
                    # dp[i] = min(dp[i], dp[j] + 1 + (d - 1))
                    dp[i] = min(dp[i], dp[j] + i // j)
        return dp[n]

        # # O(logN)
        # s = 0
        # for d in range(2, n+1):
        #     while n%d == 0:
        #         s += d
        #         n /= d
        # return s


print Solution().minSteps(32)
print Solution().minSteps(100)
