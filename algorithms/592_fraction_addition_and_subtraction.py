class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        import re
        from fractions import gcd
        debris = re.split(r'([+-])', expression)
        sign = ''
        # b/a +- d/c = (bc +- ad)/ac
        b, a = 0, 1
        for i in range(len(debris)):
            if debris[i] == '':
                continue
            if debris[i] == '+' or debris[i] == '-':
                sign = debris[i]
                continue

            d, c = map(int, (sign + debris[i]).split('/'))
            sign = ''
            b, a = b * c + a * d, a * c
            f = abs(gcd(a, b))
            b, a = b / f, a / f
        return '{}/{}'.format(b, a)


# print Solution().fractionAddition('-1/2+1/2')
# print Solution().fractionAddition('-1/2+1/2+1/3')
# print Solution().fractionAddition('1/3-1/2')
# print Solution().fractionAddition('5/3+1/3')
print Solution().fractionAddition('1/3-1/2')
