# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # abs(height(left tree) - height(right tree)) < 2
        if not root:
            return True
        return abs(self.height(root.left) - self.height(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
            
        
    def height(self, node):
        if not node:
            return 0
        left = self.height(node.left)
        right = self.height(node.right)
        return max(left, right)+1