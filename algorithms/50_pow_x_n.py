class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        # divide and conquer
        if n == 0:
            return 1
        if n<0:
            n = -n
            reciprocal = True
        else:
            reciprocal = False
        mid, odd = divmod(n, 2)
        half = self.myPow(x, mid)
        result = half*half * (x if odd else 1)
        return result if not reciprocal else 1/result
        
        # # TLE
        # if n == 0:
        #     return 1
        # result = 1
        # while n > 0:
        #     result *= x
        #     n -= 1
        # return result