# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # iterative
    def postorderTraversal(self, root):
        """
           :type root: TreeNode
           :rtype: List[int]
           """
        if not root:
            return []
        stack, result = [root], []
        while stack:
            node = stack.pop()
            result.insert(0, node.val)
            # right should be inserted first
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result
    
    
    # recursive
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return self.dfs(root, [])
    
    def dfs(self, node, result):
        if node.left:
            result = self.dfs(node.left, result)
        if node.right:
            result = self.dfs(node.right, result)
        return result + [node.val]