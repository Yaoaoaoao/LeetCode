class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = [[None for i in range(len(row))] for row in triangle]
        dp[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            n = len(triangle[i])
            dp[i][0] = dp[i-1][0] + triangle[i][0] # j=0
            for j in range(1, n-1):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
            dp[i][n-1] = dp[i-1][n-1-1] + triangle[i][n-1] # j=n-1
        return min(dp[-1])
                
                
print Solution().minimumTotal([[-1],[2,3],[1,-1,-3]]) #-1
print Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]) # 11