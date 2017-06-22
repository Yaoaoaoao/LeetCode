# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """

        def preorder(node):
            if not node:
                return ''
            left, right = '', ''
            if node.left:
                left = '(' + preorder(node.left) + ')'
            if node.right:
                right = '(' + preorder(node.right) + ')'
                if left == '':
                    left = '()'
            return str(node.val) + left + right
        
        return preorder(t)
