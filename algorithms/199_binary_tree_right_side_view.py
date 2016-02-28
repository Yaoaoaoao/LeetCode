# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # # My: Level ordered traversal and return the last element in each level.
        # if not root:
        #     return []
        # result = []
        # stack = [root]
        # while stack:
        #     result.append(stack[-1].val)
        #     level = []
        #     for ele in stack:
        #         if ele.left:
        #             level.append(ele.left)
        #         if ele.right:
        #             level.append(ele.right)
        #     stack = level
        # return result
    
        # discussion: https://leetcode.com/discuss/31348/my-simple-accepted-solution-java
        # 1. Each depth of the tree, we only select one node.
        # 2. View depth is current size of result list.
        if not root:
            return []
        return self.rightView(root, [], 0)
    
    def rightView(self, node, result, depth):
        # the right most node is added at the first time it was visited
        if not node:
            return
        if depth == len(result):
            result.append(node.val)
        self.rightView(node.right, result, depth+1)
        self.rightView(node.left, result, depth+1)
        return result