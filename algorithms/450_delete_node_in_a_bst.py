# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        """
        when root == key: 
            if root.left and root.right: new root = min in right
            else: new root = None
        """
        if not root:
            return None
        if root.val == key:
            left, right = root.left, root.right
            if not left and not right:
                return None
            elif not right:
                return left
            elif not left:
                return right
            else:
                # new root = min in right
                node = root.right
                while node.left:
                    node = node.left
                root.val = node.val
                root.right = self.deleteNode(root.right, root.val)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        return root


a, b, c, d, e, f, g = TreeNode(0), TreeNode(1), TreeNode(2), TreeNode(
    3), TreeNode(4), TreeNode(5), TreeNode(6)
b.left, b.right = a, c
f.left, f.right = e, g
d.left = b
d.right = f
root = Solution().deleteNode(d, 3)


def dfs(n):
    if not n: return
    print n.val
    print 'left',
    dfs(n.left)
    print
    print 'right',
    dfs(n.right)
    print
dfs(root)
