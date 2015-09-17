# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        # left sub-tree == right sub-tree
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if left==right==None:
                continue
            if (not left or not right) or left.val != right.val:
                return False
            if left.left or right.right:
                stack.append((left.left, right.right))
            if left.right or right.left:
                stack.append((left.right, right.left))
        return True
                
        