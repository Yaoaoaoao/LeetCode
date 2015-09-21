# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        import sys
        return self.valid(root, -sys.float_info.max, sys.float_info.max)
        
    def valid(self, node, small, big):
        if not node:
            return True 
        if node.val > small and node.val < big:
            left = self.valid(node.left, small, min(node.val, big))
            right = self.valid(node.right, max(node.val, small), big)
            return left and right
        else:
            return False

a = TreeNode(0)
a.left = TreeNode(-1)
print Solution().isValidBST(a)        