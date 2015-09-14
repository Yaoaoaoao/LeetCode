class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # O(n)space
        if not grid:
            return 0
        M, N = len(grid), len(grid[0])
        prev = [grid[0][0]]
        # i = 0
        for j in range(1, N):
            prev.append(prev[j-1] + grid[0][j])
        # i > 0
        for i in range(1, M):
            curr = [prev[0] + grid[i][0]]
            for j in range(1, N):
                curr.append(min(prev[j], curr[j-1]) + grid[i][j])
            prev = curr
        return prev[-1]
        
        # # O(mn)space
        # if not grid:
        #     return 0
        # M, N = len(grid), len(grid[0])
        # dp = [[0 for j in range(N)] for i in range(M)]
        # dp[0][0] = grid[0][0]
        # for i in range(1, M):
        #     dp[i][0] = dp[i-1][0] + grid[i][0]
        # for j in range(1, N):
        #     dp[0][j] = dp[0][j-1] + grid[0][j]
        # for i in range(1, M):
        #     for j in range(1, N):
        #         dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        # return dp[-1][-1]
    
print Solution().minPathSum([[1,2],[1,1]])