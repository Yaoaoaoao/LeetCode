class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or obstacleGrid[0][0]==1 or obstacleGrid[-1][-1] == 1:
            return 0
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[1 for j in range(n)] for i in range(m)]
        # i = 0
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] if obstacleGrid[0][j] == 0 else 0
            
        for i in range(1,m):
            dp[i][0] = dp[i-1][0] if obstacleGrid[i][0] == 0 else 0
            for j in range(1, n):
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) if (dp[i-1][j]!=0 or dp[i][j-1]!=0) and obstacleGrid[i][j]==0 else 0
        return dp[-1][-1]
                