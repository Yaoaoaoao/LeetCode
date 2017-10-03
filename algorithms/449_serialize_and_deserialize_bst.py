# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        stack = [(root, 0)]
        result = []
        max_level = 0
        while len(stack) > 0:
            node, level = stack.pop(0)
            if level <= max_level:
                result.append(node.val if node else 'null')
                if node and (node.left or node.right):
                    max_level = max(max_level, level + 1)
                    stack.append((node.left, level + 1))
                    stack.append((node.right, level + 1))
                else:
                    stack.append((None, level + 1))
                    stack.append((None, level + 1))
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = [None if d == 'null' else d for d in data]
        root = TreeNode(data[0])
        # level order traveral
        d = data[1:]
        stack = [root]
        level = 1
        while len(d) > 0:
            count = 2 ** level
            nums = d[:count]
            i = 0
            while i < len(nums):
                node = stack.pop(0)
                l = TreeNode(nums[i]) if nums[i] is not None else None
                r = TreeNode(nums[i + 1]) if nums[i + 1] is not None else None
                if node:
                    node.left = l
                    node.right = r
                stack.append(l)
                stack.append(r)
                i += 2
            d = d[count:]
            level += 1
        return root


# Your Codec object will be instantiated and called as such:
codec = Codec()
# root = TreeNode(1)
# root.right = TreeNode(2)
# print codec.deserialize(codec.serialize(root))
print codec.serialize(codec.deserialize([1, 'null', 2]))
# print codec.serialize(codec.deserialize([2, 3, 4, 5, 6, 8, 9]))
# print codec.serialize(codec.deserialize([41,37,44,24,39,42,48,1,35,38,40,
# 'null',43,46,49,0,2,30,36,'null','null','null','null','null','null',45,47,
# 'null','null','null','null','null',4,29,32,'null','null','null','null',
# 'null','null',3,9,26,'null',31,34,'null','null',7,11,25,27,'null','null',
# 33,'null',6,8,10,16,'null','null','null',28,'null','null',5,'null','null',
# 'null','null','null',15,19,'null','null','null','null',12,'null',18,20,
# 'null',13,17,'null','null',22,'null',14,'null','null',21,23]))
