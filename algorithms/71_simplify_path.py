class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for p in path.split('/'):
            if p == '' or p == '.':
                continue
            elif p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return '/'+'/'.join(stack)
            
    
print Solution().simplifyPath("/../") # /
print Solution().simplifyPath("/home//foo/") # /home/foo
print Solution().simplifyPath("/home/") # /home
print Solution().simplifyPath("/a/./b/../../c/") # /c
