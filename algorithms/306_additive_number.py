class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        
        brute force 
        key: try all possible first and second numbers
        Then check the rest of string
        '0' is valid, '02' is not valid
        """
        
        n = len(num)
        for i in range(1, n-2+1):
            first = num[0:i]
            if first.startswith('0') and first != '0':
                continue
            for j in range(i, n-1): # j+1 < n  at least 3 numbers are in num
                second = num[i:j+1]
                if second.startswith('0') and second != '0':
                    continue
                if self.check(num[j+1:], first, second):
                    return True
        else:
            return False
                
        
    def check(self, num, first, second):
        if len(num) == 0:
            return True
        third = str(int(first) + int(second))
        if num.startswith(third):
            return self.check(num[len(third):], second, third)
        else:
            return False



print Solution().isAdditiveNumber("123") # t
print Solution().isAdditiveNumber("101") # t
print Solution().isAdditiveNumber("1023") # f
print Solution().isAdditiveNumber("0235813") # f
print Solution().isAdditiveNumber("112358") # t
print Solution().isAdditiveNumber("0112358") # t
print Solution().isAdditiveNumber("199100199") # t
print Solution().isAdditiveNumber("199101199") # f
