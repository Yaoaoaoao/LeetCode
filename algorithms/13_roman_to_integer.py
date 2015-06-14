class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        R = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        n, last = 0, 0
        for i in list(s)[::-1]:
            v = R[i]
            if v < last:
                n -= v
            else:
                n += v
            last = v
        return n
            
    
print Solution().romanToInt('IV')
print Solution().romanToInt('MCMIV')
print Solution().romanToInt('V')
