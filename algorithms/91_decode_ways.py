class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        # if length == 0:
        #     return 1
        if length <= 1:
            return length if s != '0' else 0
        dp = [0] * length + [1]
        for i in range(length, -1, -1):
            if i <= length-1:
                dp[i] += (dp[i+1] if s[i:i+1] != '0' else 0)
            if i <= length-2:
                dp[i] += (dp[i+2] if 0 < int(s[i:i+2]) <= 26 and s[i] != '0' else 0)
        return dp[0]

print Solution().numDecodings('12345') #3
print Solution().numDecodings('12') #2
print Solution().numDecodings('11') #2
print Solution().numDecodings('10') #1
print Solution().numDecodings('0') #0
print Solution().numDecodings('01') #0
print Solution().numDecodings('') #1