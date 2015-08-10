class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        # discussion 
        result = []
        if k == 1:
            return [[i] for i in xrange(1, n+1)]
        tmp = []
        for r in self.combine(n, k-1):
            for i in xrange(r[-1]+1, n+1):
                tmp.append(r+[i])
        return tmp
        

print Solution().combine(4, 2)