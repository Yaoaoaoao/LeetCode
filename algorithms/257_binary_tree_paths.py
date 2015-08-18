# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        # dfs - stack
        if root is None:
            return []
        result, stack = [], [[root]]
        while stack: # stack of paths
            path = stack.pop()
            node = path.pop()
            path.append(str(node.val))
            if node.left is None and node.right is None:
                result.append('->'.join(path))
            if node.left:
                stack.append(path+[node.left])
            if node.right:
                stack.append(path+[node.right])
        return result
        