class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math
        result = ""
        digits = range(1, n+1)
        for i in reversed(range(1, n+1)):
            quotient, remainder = divmod(k, math.factorial(i-1))
            k -= quotient * math.factorial(i-1)
            result += str(digits.pop(quotient if remainder > 0 else quotient-1))
        return result
        
    
print Solution().getPermutation(3,4) # 231
print Solution().getPermutation(4,21) # 4213