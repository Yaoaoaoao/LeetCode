class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        n = list(str(num))
        s = sorted(n, reverse=True)
        l = len(n)
        for i in range(l):
            if n[i] != s[i]:
                j = l - n[::-1].index(s[i]) - 1
                n[i], n[j] = n[j], n[i]
                return int(''.join(n))
        return num


print Solution().maximumSwap(2736)
print Solution().maximumSwap(9973)
print Solution().maximumSwap(12335431)
