class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        dp[i][j] = longest palindrome string in s[i:j]
        """
        # Solution
        n = len(s)
        dp = [1] * n
        for j in xrange(1, len(s)):
            pre = dp[j]
            for i in reversed(xrange(0, j)):
                tmp = dp[i]
                if s[i] == s[j]:
                    dp[i] = 2 + pre if i + 1 <= j - 1 else 2
                else:
                    dp[i] = max(dp[i + 1], dp[i])
                pre = tmp
        return dp[0]
        
        #Time exceed
        l = len(s)
        dp = [[1 for _ in range(l)] for __ in range(l)]
        for j in range(1, l):
            for i in range(j - 1, -1, -1):
                if s[i] == s[j]:
                    dp[i][j] = (dp[i + 1][j - 1] + 2) if i + 2 <= j else 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][-1]


# print Solution().longestPalindromeSubseq("bbbab")
print Solution().longestPalindromeSubseq("cbbd")
