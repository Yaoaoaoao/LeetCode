# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # based on the property of binary search tree
        # left child < node < right child
        # p < root < q: root is the LCA
        # p, q < root: find LCA recursively in left child
        
        # quicker
        while root:
            if p.val < root.val < q.val or q.val < root.val < p.val:
                return root.val
            elif p.val == root.val or q.val == root.val:
                return root.val
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                root = root.right


        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root.val