class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # discussion implement
        # str.isalnum()
        # return newS == newS[::-1]
        
        s = filter(lambda x: 48<=ord(x)<=57 or 97<=ord(x)<=122, list(s.strip().lower()))
        if not s:
            return True
        left, right = 0, len(s)-1
        while left<=right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
        

print Solution().isPalindrome("A man, a plan, a canal: Panama")
print Solution().isPalindrome(".")
print Solution().isPalindrome("a.")