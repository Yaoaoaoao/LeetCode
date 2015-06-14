class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        # R = {1: 'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        s = num // 1000 * 'M' + num % 1000 // 100 * 'C' + num % 1000 % 100 // 10 * 'X' + num % 1000 % 100 % 10 * 'I'
        s = s.replace('I' * 9, 'IX')
        s = s.replace('I' * 5, 'V')
        s = s.replace('I' * 4, 'IV')
        s = s.replace('X' * 9, 'XC')
        s = s.replace('X' * 5, 'L')
        s = s.replace('X' * 4, 'XL')
        s = s.replace('C' * 9, 'CM')
        s = s.replace('C' * 5, 'D')
        s = s.replace('C' * 4, 'CD')
        return s


print Solution().intToRoman(1904) # MCMIV   
print Solution().intToRoman(5) # V   