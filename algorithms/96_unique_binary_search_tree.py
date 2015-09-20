class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        ### dp-memory
        if n<=2:
            return n
        dp = [1,1,2] + [0 for _ in range(3, n+1)]
        for ele in range(3, n+1):
            for i in range(ele):
                dp[ele] += dp[i] * dp[ele-i-1]
        return dp[n]
        
    
print Solution().numTrees(0)
print Solution().numTrees(1)
print Solution().numTrees(2)
print Solution().numTrees(3)
print Solution().numTrees(4)
print Solution().numTrees(5)
print Solution().numTrees(6) #132
        