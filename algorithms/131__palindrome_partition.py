class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return [[]]
        # dp[i] means partition way from s[0:i-1]
        dp = [[] for _ in range(len(s)+1)]
        dp[0] = [[]]
        # when i = 0, there is only one way to partition the string
        # dp[0+1] = [[s[0]]
        dp[1].append([s[0]])
        # when i > 2
        for i in range(1, len(s)):
            dp[i+1] = []
            for j in range(0, i+1):
                string = s[j:i+1]
                if self.isPalindrome(string):
                    # valid partition
                    for debris in dp[j]:
                        dp[i+1].append(debris+[string])
        return dp[-1]
                
    def isPalindrome(self, string):
        return string == string[::-1]
    
print Solution().partition('bb')
        
            