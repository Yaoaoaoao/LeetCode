class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        '''
        0   0
        1   0 1
        2   00 01 10 11 = 00 01 11 10
        3   000 001 010 011 100 101 110 111 
            = [000 001 011 010] [110 111 101 100] 
            = 2's, 1=reverse(2's)
            
        2   0 1 3 2
        3   0 1 3 2 6 7 5 4
            0 1 3 2 [2+4, 3+4, 1+4, 0+4]
        '''
        result = [0]
        for digit in range(n):
            result += [element+2**digit for element in reversed(result)]
        return  result
        
        
        
print Solution().grayCode(3)