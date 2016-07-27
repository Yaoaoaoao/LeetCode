class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        dp[i] = max product of number i
        Runtime: n^2
        """
        dp = [0] + [1 for i in range(n)]
        if n <= 2:
            return dp[n]
        for i in range(3, n+1):
            product = []
            for j in range(2, i):
                product.append(max(j, dp[j])*max(i-j, dp[i-j]))
            dp[i] = max(product)
        return dp[-1]

print Solution().integerBreak(2)
print Solution().integerBreak(3)
print Solution().integerBreak(4)
print Solution().integerBreak(10)