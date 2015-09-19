# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        queue = [(root, 0)]
        result = []
        while queue:
            node, level = queue.pop(0)
            if len(result) < level+1:
                result.append([])
            result[level].append(node.val)
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        for i in range(1, len(result), 2):
            result[i] = list(reversed(result[i]))
        return result