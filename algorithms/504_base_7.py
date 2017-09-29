class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            negative = True
            num = -num
        else:
            negative = False

        base = [1, 7, 49, 343, 2401, 16807, 117649, 823543, 5764801]
        result = []
        for i, b in list(enumerate(base))[::-1]:
            if num > 0 and num / b >= 1:
                result.append(str(num / b))
                num = num % b
            elif len(result) > 0:
                result.append('0')
        if len(result) == 0:
            return '0'
        else:
            return ('-' if negative else '') + ''.join(result)

    # slower
    def convertToBase7(self, num):
        if num < 0: 
            return '-' + self.convertToBase7(-num)
        if num < 7: 
            return str(num)
        return self.convertToBase7(num // 7) + str(num % 7)


print Solution().convertToBase7(100)
print Solution().convertToBase7(-7)
