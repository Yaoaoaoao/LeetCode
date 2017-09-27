class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.replace('()', '')
        left = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '*':
                left.append(s[i])
            elif s[i] == ')':
                if len(left) == 0:
                    return False
                else:
                    x = len(left) - 1
                    while x >= 0 and left[x] == '*':
                        x -= 1
                    left.pop(x)
        right = []          
        for i in range(len(left)-1, -1, -1):
            if left[i] == ')' or left[i] == '*':
                right.append(left[i])
            elif left[i] == '(':
                if len(right) == 0:
                    return False
                else:
                    x = len(right) - 1
                    while x >= 0 and right[x] == '*':
                        x -= 1
                    right.pop(x)
        for i in right:
            if i != '*':
                return False
        return True
        
print Solution().checkValidString('()')
print Solution().checkValidString('(*)')
print Solution().checkValidString('(*))')
print Solution().checkValidString('(*()')