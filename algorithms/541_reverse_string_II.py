class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        reverse = True
        result = ''
        for i in range(0, len(s), k):
            piece = s[i:i + k]
            result += piece[::-1] if reverse else piece
            reverse = not reverse
        return result


print Solution().reverseStr('abcdefg', 2)
