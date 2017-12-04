class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        b = bin(n)[2:]
        for i in xrange(1, len(b)):
            if b[i] == b[i-1]:
                return False
        return True
        
        binary = bin(n)[2:]
        if '00' in binary:
            return False
        if '11' in binary:
            return False
        return True