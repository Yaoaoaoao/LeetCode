class Solution:
    # @param {integer} num
    # @return {integer}
    def addDigits(self, num):
        # discussion digital root
        # https://en.wikipedia.org/wiki/Digital_root
        if num==0:
            return 0
        elif num%9 == 0:
            return 9
        else:
            return num%9
        
        # my solution
        sum = 0
        while num:
            sum += num%10
            num = num//10
        return self.addDigits(sum) if sum//10 else sum
    
print Solution().addDigits(0)
print Solution().addDigits(38)