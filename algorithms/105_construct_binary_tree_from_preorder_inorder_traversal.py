# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not preorder:
            return None
        
        rootVal = preorder.pop(0)
        rootIdx = inorder.index(rootVal)
        
        root = TreeNode(rootVal)
        root.left = self.buildTree(preorder, inorder[:rootIdx])
        root.right = self.buildTree(preorder, inorder[rootIdx+1:])
        
        return root
        