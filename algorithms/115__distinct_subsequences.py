class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # dp[i][j] means distinct subsequences for S[:i] and T[:j]
        m, n = len(s), len(t)
        if n>m:
            return 0 
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        # when t='', s can match it by delete all letters. 
        for i in range(m+1):
            dp[i][0] = 1
            
        for i in range(1, m+1):
            for j in range(1, n+1):
                # delete s new letter + if s[-1] == t[-1]
                dp[i][j] = dp[i-1][j] + (dp[i-1][j-1] if s[i-1] == t[j-1] else 0)
        return dp[-1][-1]
    
        
print Solution().numDistinct('rabbbit', 'rabbit')