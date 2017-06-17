class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a1, a2 = map(int, a[:-1].split('+'))
        b1, b2 = map(int, b[:-1].split('+'))
        return '%d+%di' % (a1 * b1 - a2 * b2, a1 * b2 + a2 * b1)

    def complexNumberMultiply(self, m, n):
        def evaluate(num):
            idx = num.find('+')
            x = int(num[:idx])
            y = int(num[idx + 1:-1])
            return x, y

        a, b = evaluate(m)
        c, d = evaluate(n)
        # result: u + vi
        u = a * c - b * d
        v = a * d + b * c
        return str(u) + '+' + str(v) + 'i'


print Solution().complexNumberMultiply("1+1i", "1+1i")
print Solution().complexNumberMultiply("1+-1i", "1+-1i")
