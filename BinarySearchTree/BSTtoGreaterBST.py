# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.sumA = 0

        def returnTree(node):
            if node == None:
                return None
            if node.left == None and node.right == None:
                self.sumA += node.val
                return TreeNode(self.sumA)
            aux = TreeNode()
            aux.right = returnTree(node.right)
            self.sumA += node.val
            aux.val = self.sumA
            aux.left = returnTree(node.left)
            return aux
        return returnTree(root)
