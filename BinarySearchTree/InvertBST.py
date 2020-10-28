# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def invert(node):
            if node == None:
                return None
            return TreeNode(node.val, invert(node.right), invert(node.left))
        return invert(root)
