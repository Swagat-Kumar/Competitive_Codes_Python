# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        self.st = ""

        def encode(node):
            if node == None:
                self.st += '.,'
                return
            self.st += str(node.val)+','
            encode(node.left)
            encode(node.right)
        encode(root)
        return self.st[:len(self.st)-1]

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        print(data)
        listD = list(data.split(','))
        print(listD)
        self.i = 0

        def returnTree():
            if listD[self.i] == '.':
                return None
            aux = TreeNode(int(listD[self.i]))
            self.i += 1
            aux.left = returnTree()
            self.i += 1
            aux.right = returnTree()
            return aux
        return returnTree()

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
