# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        #dfs
        if root:
            stack = [root]
            while stack:
                node = stack.pop()
                node.left, node.right = node.right, node.left
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return root