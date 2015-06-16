class Solution:
    # @param {integer} n
    # @return {string[]}
    # My solution 52ms
    def generateParenthesis(self, n):
        if n==0:
            return ['']
        return self.add_parenthesis(n-1, ['()'])
        
    def add_parenthesis(self, n, prev):
        if n == 0:
            return prev
        else:
            res = {}
            for s in prev:
                for i in range(len(s)):
                    new = s[:i]+'()'+s[i:]
                    if new not in res:
                        res[new]=None
            n -= 1
            return self.add_parenthesis(n, res.keys())


    # c++ solution 88ms
    def generateParenthesis(self, n):
        l = self.add_parenthesis([], '', n, 0)
        return l
        
    def add_parenthesis(self, l, s, n, m):
        # print n, m 
        if n==0 and m==0:
            l.append(s)
            return l 
        if m>0:
            self.add_parenthesis(l, s+')', n, m-1)
        if n>0:
            self.add_parenthesis(l, s+'(', n-1, m+1)
        return l
        
        
        
print Solution().generateParenthesis(0)
print Solution().generateParenthesis(1)
print Solution().generateParenthesis(2)
print Solution().generateParenthesis(3)
print Solution().generateParenthesis(4)