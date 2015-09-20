# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        while root and root.left:
            cur = root.left
            prev = None
            while root:
                if prev:
                    prev.next = root.left
                root.left.next = root.right
                prev = root.right
                root = root.next
            root = cur