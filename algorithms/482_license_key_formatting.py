class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = S.replace('-', '').upper()
        rst = ''
        i = len(s)
        while i > 0:
            rst = s[max(0, i - K):i] + '-' + rst
            i -= K
        return rst[:-1]


print Solution().licenseKeyFormatting('2-4A0r7-4k', 4)  # "24A0-R74K"
print Solution().licenseKeyFormatting('2-4A0r7-4k', 3)  # "24-A0R-74K"
