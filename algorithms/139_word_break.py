class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if not wordDict:
            return False
        dp = [True] + [False for _ in range(len(s))]
        for i in range(1, len(s)+1):
            for word in wordDict:
                wordLen = len(word)
                if i < wordLen:
                    dp[i] = dp[i] or False
                else:
                    if s[i-wordLen:i] == word and dp[i-wordLen]:
                        dp[i] = dp[i] or True
        return dp[-1]
    
# print Solution().wordBreak('a', ['a'])
print Solution().wordBreak("bb", ["a","b","bbb","bbbb"])