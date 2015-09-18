class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        result = []
        cycle = {}
        
        negativeSign = ''
        if numerator*denominator<0:
            negativeSign = '-'
        numerator, denominator = abs(numerator), abs(denominator)
        quotient,remainder = divmod(numerator, denominator)
        result.append(negativeSign+quotient)
        
        while remainder!=0:
            quotient,remainder = divmod(remainder*10, denominator)
            if remainder not in cycle:
                cycle[remainder] = len(result)
                result.append(quotient)
            else:
                repeatStart = cycle[remainder]
                if result[repeatStart] != quotient:
                    result.append(quotient)
                    repeatStart += 1
                result = map(str, result)
                unrepeat = ''.join(result[1:repeatStart]) if repeatStart > 1 else ''  
                repeat = ''.join(result[repeatStart:])
                return  result[0] + '.%s(%s)' % (unrepeat, repeat)
        result = map(str, result)
        return result[0] + ('.%s' % (''.join(result[1:])) if len(result)>1 else '')
    
# print Solution().fractionToDecimal(1,2)
# print Solution().fractionToDecimal(2,1)
# print Solution().fractionToDecimal(2,3)
# print Solution().fractionToDecimal(1,6)
print Solution().fractionToDecimal(-50, 8)
print Solution().fractionToDecimal(7, -12)