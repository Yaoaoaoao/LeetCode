class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        nlen = len(needle)
        if len(haystack) < nlen:
            return -1
        if nlen == 0:
            return 0
        for h in range(len(haystack)-nlen+1):
            if haystack[h:h+nlen] == needle:
                return h
        else:
            return -1
        
print Solution().strStr("a", "a")