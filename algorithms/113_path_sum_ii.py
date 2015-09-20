# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        # !!! root-to-leaf paths
        if not root:
            return []
        result = []
        stack = [(root, root.val, [root.val])] # node, sum, path
        while stack:
            node, sum_, path = stack.pop()
            if sum_ == sum and not node.left and not node.right:
                result.append(path)
            if node.left:
                stack.append((node.left, sum_+node.left.val, path+[node.left.val]))
            if node.right:
                stack.append((node.right, sum_+node.right.val, path+[node.right.val]))
        return result
