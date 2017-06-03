# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # post-order traversal O(n)
        self.tilt = 0

        def dfs(node):
            if not node:
                return
            if node.left:
                dfs(node.left)
                left = node.left.sum_of_subtree
            else:
                left = 0
            if node.right:
                dfs(node.right)
                right = node.right.sum_of_subtree
            else:
                right = 0
            node.sum_of_subtree = node.val + left + right
            self.tilt += abs(left - right)

        dfs(root)
        return self.tilt
