# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        levels = []
        stack = [(root, 0)]
        while len(stack) > 0:
            node, level = stack.pop(0)
            if level + 1 > len(levels):
                levels.append([])
            levels[level].append(node.val)
            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))
        return [1.0 * sum(l) / len(l) for l in levels]
