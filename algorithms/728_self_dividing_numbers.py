class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def check(num):
            digits = set(map(int, str(num)))
            if 0 in digits:
                return False
            for digit in digits:
                if digit == 1:
                    continue
                if num % digit != 0:
                    return False
            return True
        
        result = []
        for num in range(left, right+1):
            if check(num):
                result.append(num)
                
        return result
        
print Solution().selfDividingNumbers(1, 22)
                