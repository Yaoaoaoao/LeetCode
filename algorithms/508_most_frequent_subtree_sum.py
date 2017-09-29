# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result = []
        self.calculate_sum(root, result)
        from collections import Counter
        s = sorted(Counter(result).items(), key=lambda x: x[1], reverse=True)
        result = [s[0][0]]
        for i in range(1, len(s)):
            if s[i][1] == s[i - 1][1]:
                result.append(s[i][0])
            else:
                break
        return result

    def calculate_sum(self, node, result):
        if not node:
            return 0
        node.sum = node.val + self.calculate_sum(node.left, result) + self.calculate_sum( node.right, result)
        result.append(node.sum)
        return node.sum


root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(-3)
print Solution().findFrequentTreeSum(root)
