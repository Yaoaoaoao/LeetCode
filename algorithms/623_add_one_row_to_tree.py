# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            new = TreeNode(v)
            new.left = root
            return new
        stack = [(root, 1)]
        while len(stack) > 0:
            node, level = stack.pop(0)
            if not node: 
                continue
            if level == d - 1:
                newLeft = TreeNode(v)
                newRight = TreeNode(v)
                newLeft.left = node.left
                newRight.right = node.right
                node.left = newLeft
                node.right = newRight
            elif level > d:
                break
            else:
                stack.append((node.left, level + 1))
                stack.append((node.right, level + 1))
        return root