# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # iteratively
        if not root:
            return []
        stack, result = [root], []
        while stack:
            node = stack.pop()
            result.append(node.val)
            # right first, visit last
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result
                
    
    # recursive
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return self.dfs(root, [])
    
    def dfs(self, node, result):
        result += [node.val]
        if node.left:
            result = self.dfs(node.left, result)
        if node.right:
            result = self.dfs(node.right, result)
        return result
    
print Solution().preorderTraversal(TreeNode(1))