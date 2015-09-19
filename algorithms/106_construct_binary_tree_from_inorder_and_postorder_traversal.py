# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        
        # root = last of postorder
        # inorder: element after root will be on the right branch
        root = TreeNode(postorder.pop())
        rootIdx = inorder.index(root.val)
        
        rightBranch = inorder[rootIdx+1:]
        leftBranch = inorder[:rootIdx]
        
        root.right = self.buildTree(rightBranch, postorder)
        root.left = self.buildTree(leftBranch, postorder)
        
        return root
        
        