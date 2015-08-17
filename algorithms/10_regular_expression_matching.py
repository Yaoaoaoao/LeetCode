class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        slength, plength = len(s), len(p)
        # dp[i][j] means string[0:i] matches pattern[0:j]
        dp = [[None for i in range(plength+1)] for i in range(slength+1)]
        dp[0][0] = True
        
        # when i == 0, pattern is empty, False
        # when j == 0, string is empty
        for j in range(1, plength):
            # if pattern is *
            dp[0][j+1] = dp[0][j-1] and p[j] == '*'
        
        # when i > 0 and j > 0
        for i in range(slength):
            for j in range(plength):
                if p[j] == '*':
                    # determine dp[3][4] aab = c*a*
                    # match no preceding character (from two above) dp[3][2] = F : aab = c*
                    # match more preceding character (from above) dp[3][3] = F : aab = c*a
                    # if the new character in string matches pattern's preceding character (from left) dp[2][4] = T : aa = c*a*
                    dp[i+1][j+1] = dp[i+1][j-1] or dp[i+1][j] or (dp[i][j+1] and (p[j-1] == '.' or s[i] == p[j-1]))
                else:
                    dp[i+1][j+1] = dp[i][j] and (p[j] == '.' or s[i] == p[j])
        print dp
        return dp[slength][plength]
    
# print Solution().isMatch('aa', 'a') # false
# print Solution().isMatch('aaa', 'aa') # false
# print Solution().isMatch('aa', 'a*') # true
# print Solution().isMatch('aa', '.*') # true
print Solution().isMatch('aab', 'c*a*b') # true
# print Solution().isMatch("abcd", "d*") # false
# print Solution().isMatch("a", "ab*a") # false
# print Solution().isMatch("aaa", "ab*a*c*a") # true