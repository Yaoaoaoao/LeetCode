class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        if len(s)==0:
            return 0
        A = [False for i in range(len(s))]
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if len(stack)>0:
                    A[stack.pop(-1)] = A[i] = True
                else:
                    stack = []
        maxLen = curLen = 0
        for i in range(0, len(A)):
            if A[i]:
                curLen += 1
            else:
                maxLen = max(maxLen, curLen)
                curLen = 0
        maxLen = max(maxLen, curLen)
        return maxLen
    
print Solution().longestValidParentheses('(') #0
print Solution().longestValidParentheses('()') #2
print Solution().longestValidParentheses('()(()') #2
print Solution().longestValidParentheses(')()())') #4
print Solution().longestValidParentheses(')()()())()))') #6