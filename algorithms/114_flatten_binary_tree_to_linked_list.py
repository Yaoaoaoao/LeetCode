# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        # preorder traversal
        stack = [root]
        preorder = []
        while stack:
            node = stack.pop()
            preorder.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
        for node in range(len(preorder)-1):
            preorder[node].left = None
            preorder[node].right = preorder[node+1]
        preorder[-1].left = None
        preorder[-1].right = None
    