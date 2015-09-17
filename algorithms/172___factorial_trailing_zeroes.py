class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 10 = 2*5
        # 5! = 1.5 = 2.3.4.5 -> 1*10
        # 10! = 2.5 = 2.3.4.5.6.7.8.9.10 -> 2.10
        # 15! = 3.5 = 2.3.4.5.6.7.8.9.10.11.12.13.14.15 -> 3.10
        # so check number of factor = 5, then 25, then 125 ... 
        
        factor = 5
        result = 0
        while n >= factor:
            result += n/factor
            factor *= 5
        return result
        
    
print Solution().trailingZeroes(3950) #986
    
