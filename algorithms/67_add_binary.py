class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return str(bin(int(a,2)+int(b,2)))[2:] # remove 0b
    
print Solution().addBinary("11", "1") # 100