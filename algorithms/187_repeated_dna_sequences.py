class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        pool = {}
        ans = {}
        for i in xrange(0, len(s)-10+1):
            k = s[i:i+10]
            if k in pool:
                ans[k] = None
            else:
                pool[k] = None
        return ans.keys()
        
        
print Solution().findRepeatedDnaSequences("AGCTAGCTAGCTAGCTAGCT")