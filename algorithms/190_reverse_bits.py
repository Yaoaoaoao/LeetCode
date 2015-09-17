class Solution(object):
    def reverseBits(self, n):
        oribin='{0:032b}'.format(n)
        reversebin=oribin[::-1]
        return int(reversebin,2)
    
    # my 56 ms
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        number = str(bin(n))[::-1]
        number = number[:-2] + '0'*(32-len(number)+2)
        return int(number,2)
        
print Solution().reverseBits(1)
print Solution().reverseBits(2)
print Solution().reverseBits(43261596)

# 2147483648
# 1073741824
# 964176192
