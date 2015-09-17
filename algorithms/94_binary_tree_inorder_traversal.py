# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        node = root
        stack = []
        result = []
        while node or stack:
            # find the left most node
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.val)
            node = node.right
        return result
            


    # recursive
    def inorderTraversal(self, root):
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
        result += [node.val]
        if node.right:
            result = self.dfs(node.right, result)
        return result
