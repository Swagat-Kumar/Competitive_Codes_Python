# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def visit(node):
            if node == None:
                return None
            if node.val == 0 and visit(node.left) == None and visit(node.right) == None:
                return None
            else:
                return TreeNode(node.val, visit(node.left), visit(node.right))
        return visit(root)
