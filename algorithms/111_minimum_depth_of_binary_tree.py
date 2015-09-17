# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# shortest path from the root node down to the nearest leaf node
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # dfs
        if not root:
            return 0
        stack = [(root,0)]
        minLevel = None
        while stack:
            node, level = stack.pop()
            if node.left:
                stack.append((node.left, level+1))
            if node.right:
                stack.append((node.right, level+1))
            if not node.left and not node.right:
                minLevel = (level + 1) if not minLevel else min(minLevel, level+1)
        return minLevel