# follow leetcode serialization method.
# using binary tree level order traversal.
# null means a path is terminated (no node exists below)

# To read leetcode input, use json.
import json

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
        stack, traversal = [root], []
        while stack:
            level, next_level = [], []
            for node in stack:
                if node:
                    level.append(node.val)
                    next_level.append(node.left)
                    next_level.append(node.right)
                else:
                    # level.append("null") # to pass OJ
                    level.append(None)
            traversal.extend(level)
            stack = next_level
        # while traversal[-1] == "null": # to pass OJ
        while not traversal[-1]:
            traversal.pop()
        return json.dumps(traversal)
                

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = json.loads(data)
        return self.__decode_tree(data, 0)
    
    def __decode_tree(self, data, i):
        if i >= len(data):
            return None
        node = TreeNode(data[i])
        left, right = 2*i+1, 2*i+2
        node.left = self.__decode_tree(data, left)
        node.right = self.__decode_tree(data, right)
        return node

def generate_tree(code):
    return Codec().deserialize(code)

if __name__=="__main__":
    # Your Codec object will be instantiated and called as such:
    codec = Codec()
    code = "[1, 2, 3, null, null, 4, 5]"
    tree = codec.serialize(codec.deserialize(code))
    print code == tree