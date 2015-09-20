# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        leftDepth = self.get_depth(root.left)
        rightDepth = self.get_depth(root.right)
        if leftDepth == rightDepth:
            return 2**leftDepth + self.countNodes(root.right)
        else:
            return 2**rightDepth + self.countNodes(root.left)
       
    def get_depth(self, node): 
        depth = 0
        while node:
            node = node.left
            depth += 1
        return depth