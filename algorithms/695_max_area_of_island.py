class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        def island(i, j, count):
            if grid[i][j] == 1:
                grid[i][j] = 2
                count += 1
                if i > 0:
                    count = island(i - 1, j, count)
                if i < m - 1:
                    count = island(i + 1, j, count)
                if j > 0:
                    count = island(i, j - 1, count)
                if j < n - 1:
                    count = island(i, j + 1, count)
            return count

        max_size = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    size = island(i, j, 0)
                    max_size = max(max_size, size)
        return max_size


# print Solution().maxAreaOfIsland(
#     [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]])

print Solution().maxAreaOfIsland(
    [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]])
# 
# print Solution().maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#                                   [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
#                                   [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#                                   [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
#                                   [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
#                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#                                   [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
#                                   [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]])
