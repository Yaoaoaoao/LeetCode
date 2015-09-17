class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 1:
            return ''
        result = ''
        while n > 0:
            remainder = n%26
            n = n//26
            if remainder == 0:
                result = chr(26+64) + result
                n -= 1
            else:
                result = chr(remainder+64) + result
        return result
    
print Solution().convertToTitle(26)
print Solution().convertToTitle(27)
print Solution().convertToTitle(53)