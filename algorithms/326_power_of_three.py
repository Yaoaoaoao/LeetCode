class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        "largest power of 3 under int is 1162261467"
        return True if n>0 and 1162261467%n == 0 else False