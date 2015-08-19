class Solution:
    # @param {integer} num
    # @return {boolean}
    def isUgly(self, num):
        if num <= 0:
            return False
        # continue divide the number by 2, 3 and 5
        # if ugly the leftover is 1
        for i in [2,3,5]:
            while (num%i==0):
                num /= i
        return num == 1
    
print Solution().isUgly(0)
print Solution().isUgly(1)
print Solution().isUgly(6)
print Solution().isUgly(8)
print Solution().isUgly(14)
