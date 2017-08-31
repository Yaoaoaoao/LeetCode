class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        maxfactor = int(c ** 0.5)
        for a in range(maxfactor + 1):
            b2 = c - a * a
            b = b2 ** 0.5
            if int(b) == b:
                return True
        return False

print Solution().judgeSquareSum(5)
print Solution().judgeSquareSum(3)
print Solution().judgeSquareSum(1)
