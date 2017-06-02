# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        # dfs s 
        stack = [s]
        while len(stack) > 0:
            node = stack.pop(-1)
            if node.val == t.val:
                rst = self.check_subtree(node, t)
                if rst:
                    return True
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return False

    def check_subtree(self, a, b):
        stack = [(a, b)]
        while len(stack) > 0:
            na, nb = stack.pop(-1)
            if na is None and nb is None:
                continue
            elif na is None or nb is None:
                return False
            else:
                if na.val != nb.val:
                    return False
                stack.append((na.right, nb.right))
                stack.append((na.left, nb.left))
        return True
    
    
"""
[3,4,5,1,2,null,null,0]
[4,1,2]

[3,4,5,1,2]
[4,1,2]
"""