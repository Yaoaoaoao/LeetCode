class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        # Solution O(nlgn)
        pairs = sorted(pairs, key=lambda x: x[0])
        result = 1
        end = pairs[0][1]
        for i in xrange(1, len(pairs)):
            if pairs[i][0] <= end:
                end = min(end, pairs[i][1])
            else:
                result += 1
                end = pairs[i][1]
        return result

        # dp[i] = max(dp[0~i-1] + 1?) O(nlgn)+O(n**2)
        l = len(pairs)
        if l == 0:
            return 0
        dp = [0] * l
        pairs = sorted(pairs, key=lambda x: x[0])
        for i in range(l):
            m = 1
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    m = max(dp[j] + 1, m)
                else:
                    m = max(dp[j], m)
            dp[i] = m
        return dp[-1]


print Solution().findLongestChain([])
print Solution().findLongestChain([[1, 2], [2, 3], [3, 4]])
print Solution().findLongestChain([[3, 4], [2, 3], [1, 2]])
print Solution().findLongestChain([[1, 5], [1, 2], [2, 3], [3, 4], [5, 6]])
