class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1]:
            return True
        else:
            start, end = 0, len(s) - 1
            while start <= end: 
                if s[start] != s[end]:
                    # delete s[start]
                    delete_left = s[:start] + s[start+1:]
                    delete_right = s[:end] + s[end+1:]
                    if delete_left == delete_left[::-1] or \
                            delete_right == delete_right[::-1]:
                        return True
                    else:
                        return False
                start += 1
                end -= 1
        
        # Time Limit Exceeded 
        if s == s[::-1]:
            return True
        else:
            l = len(s)
            for i in range(l):
                new = s[:i] + s[i+1:]
                if new == new[::-1]:
                    return True
            return False

print Solution().validPalindrome('abca')