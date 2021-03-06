# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # bfs
        if not root:
            return []
        result = []
        queue = [(root, 0)]
        while queue:
            node, level = queue.pop(0)
            if len(result) < level+1:
                result.insert(0, [])
            result[-(level+1)].append(node.val)
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        return result
        # or use 102 with list(reversed(result))
        