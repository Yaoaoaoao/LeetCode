class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        p = {')': '(', ']':'[', '}':'{'}
        s = list(s)
        stack = []
        while len(s)>0:
            if s[0] in ['(', '[', '{']:
                stack.append(s[0])
            else:
                if len(stack) < 1 or p[s[0]] != stack[-1]:
                    return False
                else:
                    stack.pop(-1)
            s.pop(0)
        return not stack
        
        
        M = {'(':')', '[':']', '{':'}'}
        stack = []
        for p in s:
            if p in M:
                stack.append(M[p])
            else:
                if not stack or p != stack.pop():
                    return False
                
        return not stack

print Solution().isValid('()[]{}')
print Solution().isValid('([)]')
print Solution().isValid(']')
print Solution().isValid('[')
