# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # dfs - stack
        if not root:
            return False
            
        stack = [(root, 0)]
        explored = {}
        
        while stack:
            node, sum_ = stack.pop()
            explored[node] = True
            sum_ += node.val
            
            if not node.left and not node.right and sum_ == sum:
                return True
            
            if node.left and not explored.get(node.left, False):
                stack.append((node.left, sum_))
            if node.right and not explored.get(node.right, False):
                stack.append((node.right, sum_))
        else:
            return False
                
        
                