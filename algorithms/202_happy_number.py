class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #s1 64ms
        meet = {}
        while n != 1:
            sum_ = sum([int(i)**2 for i in str(n)])
            if sum_ in meet:
                return False
            meet[sum_] = None
            n = sum_
        return True

    
    
    # s2 60ms
    # def isHappy(self, n):
    #     """
    #     :type n: int
    #     :rtype: bool
    #     """
    #     meet = {}
    #     while n > 0:
    #         sum_ = self.squareSum(n)
    #         if sum_ == 1:
    #             return True
    #         if sum_ in meet:
    #             return False
    #         meet[sum_] = None
    #         n = sum_
    #     return False
    #     
    # def squareSum(self, n):
    #     sum_ = 0
    #     while n > 0:
    #         digit = n%10
    #         sum_ += digit**2
    #         n = n//10
    #     return sum_
    
print Solution().isHappy(19)