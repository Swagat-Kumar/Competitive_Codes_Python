# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def visit(node):
            if node == None:
                return None
            if node.val >= low and node.val <= high:
                return TreeNode(node.val, visit(node.left), visit(node.right))
            elif node.val > high:
                return visit(node.left)
            else:
                return visit(node.right)
        return visit(root)
