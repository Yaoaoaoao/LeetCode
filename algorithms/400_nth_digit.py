class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 1-9: 9*1=9  10^0
        # 10-99: 9*10=90  10^1
        # 100-999: 9*100=900  10^2
        n -= 1
        for digit in range(1, 11):
            first, last = 10 ** (digit - 1), 10 ** digit - 1
            total_digits = 9 * first * digit
            if n < total_digits:
                d, m = divmod(n, digit)
                return int(str(first + d)[m])
            n -= total_digits


print Solution().findNthDigit(45)  # 7
print Solution().findNthDigit(17000)  # 2
