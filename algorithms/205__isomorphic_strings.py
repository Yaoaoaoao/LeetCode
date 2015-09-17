class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        return len(set(zip(s, t)))==len(set(s))==len(set(t))

print Solution().isIsomorphic("ab", "aa") # false
print Solution().isIsomorphic('egg', 'add') # true
print Solution().isIsomorphic('foo', 'bar') # false
print Solution().isIsomorphic('paper', 'title') # true
