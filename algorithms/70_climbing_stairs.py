class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # fibonacci number
        a = b = 1
        for i in range(1, n):
            a, b = b, a+b
        return b

print Solution().climbStairs(5)