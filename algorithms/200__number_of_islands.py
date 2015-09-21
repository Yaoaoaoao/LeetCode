class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        count = 0
        
        def dfs(x, y):
            if not (0 <= x < m and 0 <= y < n):
                return
            if grid[x][y] != '1':
                return
            grid[x][y] = True # label visit
            dfs(x+1, y) # bottom
            dfs(x, y+1) # right
            dfs(x-1, y) # top
            dfs(x, y-1) # left
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count