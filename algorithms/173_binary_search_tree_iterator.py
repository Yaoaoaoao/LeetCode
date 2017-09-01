# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.findLeftMost(root)

    def findLeftMost(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop(-1)
        self.findLeftMost(node.right)
        return node.val


# Your BSTIterator will be called like this:
root = TreeNode(2)
root.left = TreeNode(1)
i, v = BSTIterator(root), []
while i.hasNext():
    v.append(i.next())
print v
