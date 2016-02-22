class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]
        result = []
        for i in range(len(input)):
            if input[i] in "+-*":
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                result.extend([eval(str(j)+input[i]+str(k)) for k in right for j in left] )
        return result
        
        
print Solution().diffWaysToCompute("0")
print Solution().diffWaysToCompute("2-1-1")
print Solution().diffWaysToCompute("2*3-4*5")