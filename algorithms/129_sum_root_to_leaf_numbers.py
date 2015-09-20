# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        total = 0
        stack = [(root, root.val)]
        while stack:
            node, sum_ = stack.pop()
            if not node.left and not node.right: # leaf
                total += sum_
            if node.left:
                stack.append((node.left, sum_*10+node.left.val))
            if node.right:
                stack.append((node.right, sum_*10+node.right.val))
        return total