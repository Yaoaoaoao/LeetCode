class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        if s==t: 
            return True
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = t[i]
        for i in range(len(s)):
            print i, t[i], d[s[i]]
            if s[i] != d[s[i]]:
                return False
        else:
            return True
    
print Solution().isIsomorphic("ab", "aa") # false
print Solution().isIsomorphic('egg', 'add') # true
print Solution().isIsomorphic('foo', 'bar') # false
print Solution().isIsomorphic('paper', 'title') # true
