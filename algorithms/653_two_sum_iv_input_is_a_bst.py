# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        values = set()
        stack = [root]
        while len(stack) > 0:
            node = stack.pop(0)
            values.add(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        for i in values:
            if (k - i) in values and i != k-i:
                return True
        return False
