class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(reversed(s.strip().split()))
    
print Solution().reverseWords(" ")
print Solution().reverseWords("   a   b ")
print Solution().reverseWords("the sky is blue")