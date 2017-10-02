class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """

        def calcStep(r, c):
            if r < 0 or c < 0 or r >= N or c >= N:
                return 0
            else:
                return prev[r][c]

        def step(r, c):
            prob = 0.0
            prob += 0.125 * calcStep(r + 1, c - 2)
            prob += 0.125 * calcStep(r + 1, c + 2)
            prob += 0.125 * calcStep(r + 2, c - 1)
            prob += 0.125 * calcStep(r + 2, c + 1)
            prob += 0.125 * calcStep(r - 1, c - 2)
            prob += 0.125 * calcStep(r - 1, c + 2)
            prob += 0.125 * calcStep(r - 2, c - 1)
            prob += 0.125 * calcStep(r - 2, c + 1)
            return prob

        if not K:
            return 1
        
        prev = [[0 for x in range(N)] for y in range(N)]
        prev[r][c] = 1

        for _ in range(K):
            dp = [[0 for x in range(N)] for y in range(N)]
            for i in range(N):
                for j in range(N):
                    dp[i][j] = step(i, j)
            prev = dp
        return sum([sum(i) for i in prev])


print Solution().knightProbability(3, 2, 0, 0)
