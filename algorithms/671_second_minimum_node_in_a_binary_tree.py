# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        candidates = []
        stack = [root]
        while len(stack) > 0:
            node = stack.pop(0)
            if node.left and node.right:
                if node.val == node.left.val:
                    stack.append(node.left)
                else:
                    candidates.append(node.left.val)
                if node.val == node.right.val:
                    stack.append(node.right)
                else:
                    candidates.append(node.right.val)
        if len(candidates) > 0:
            return min(candidates)
        else:
            return -1
