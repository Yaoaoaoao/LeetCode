# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.pickroot(nums, 0, len(nums))

    def pickroot(self, nums, start, end):
        if start == end:
            return None
        i, n = start, nums[start]
        for m in range(start + 1, end):
            if nums[m] > n:
                i = m
                n = nums[m]
        root = TreeNode(n)
        root.left = self.pickroot(nums, start, i)
        root.right = self.pickroot(nums, i + 1, end)
        return root


print Solution().constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
