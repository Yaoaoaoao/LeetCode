# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
            0
          0   1
         0 1 2 3 
        """
        stack = [(root, 0, 0)]
        cur_depth = left = ans = 0
        while len(stack) > 0:
            node, depth, pos = stack.pop(0)
            if node:
                stack.append((node.left, depth + 1, pos * 2))
                stack.append((node.right, depth + 1, pos * 2 + 1))
                if cur_depth != depth:
                    cur_depth = depth
                    left = pos
                ans = max(pos - left + 1, ans)
        return ans
