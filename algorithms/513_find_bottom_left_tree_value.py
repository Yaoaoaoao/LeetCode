# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return []
        stack = [(root, 1)]
        result = []
        while len(stack) > 0:
            node, l = stack.pop(0)
            if l > len(result):
                result.append((node.val, l))
            if node.left:
                stack.append((node.left, l+1))
            if node.right:
                stack.append((node.right, l+1))
        return result[-1][0]
            