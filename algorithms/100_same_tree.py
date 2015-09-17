# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p or not q:
            return True if not p and not q else False
        stack = [(p, q)]
        while stack:
            pnode, qnode = stack.pop()
            if not (pnode and qnode):
                return False
            if pnode.val != qnode.val:
                return False
            if pnode.left or qnode.left:
                stack.append((pnode.left, qnode.left))
            if pnode.right or qnode.right:
                stack.append((pnode.right, qnode.right))
        return True