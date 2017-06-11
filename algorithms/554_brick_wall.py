class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """

        from collections import defaultdict
        bricks = defaultdict(lambda: 0)
        for row in wall:
            i = 0
            for brick in row[:-1]:
                i += brick
                bricks[i] += 1
        return len(wall) - (max(bricks.values()) if len(bricks) > 0 else 0)

    """
        # memory error for [[100000000], [100000000], [100000000]]
        brick_length = sum(wall[0])
        if brick_length == 1:
            return len(wall)
        obstacle = [0] * brick_length
        for row in wall:
            i = 0
            for brick in row:
                for j in range(brick - 1):
                    obstacle[i] += 1
                    i += 1
                i += 1
        return min(obstacle[:-1])
    """


print Solution().leastBricks([[1, 2, 2, 1],
                              [3, 1, 2],
                              [1, 3, 2],
                              [2, 4],
                              [3, 1, 2],
                              [1, 3, 1, 1]])
print Solution().leastBricks([[5], [5]])
print Solution().leastBricks([[1], [1], [1]])
print Solution().leastBricks([[100000000], [100000000], [100000000]])
print Solution().leastBricks(
    [[6], [6], [2, 4], [6], [1, 2, 2, 1], [6], [2, 1, 2, 1], [1, 5], [4, 1, 1],
     [1, 4, 1], [4, 2], [3, 3], [2, 2, 2], [5, 1], [5, 1], [6], [4, 2], [1, 5],
     [2, 3, 1], [4, 2], [1, 1, 4], [1, 3, 1, 1],
     [2, 3, 1], [3, 3], [3, 1, 1, 1], [3, 2, 1], [6], [3, 2, 1], [1, 5],
     [1, 4, 1]])  # 17
