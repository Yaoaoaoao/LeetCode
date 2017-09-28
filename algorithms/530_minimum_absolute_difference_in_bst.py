# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        tree = self.inorder(root, [])
        delta = tree[1] - tree[0]
        for i in range(2, len(tree)):
            delta = min(delta, tree[i] - tree[i - 1])
        return delta

    def inorder(self, node, result):
        if node.left:
            result = self.inorder(node.left, result)
        result += [node.val]
        if node.right:
            result = self.inorder(node.right, result)
        return result
