# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        def solve(node, level=1):
            if node == None:
                return None
            if level == d-1:
                return TreeNode(node.val, TreeNode(v, solve(node.left, level+1), None), TreeNode(v, None, solve(node.right, level+1)))
            return TreeNode(node.val, solve(node.left, level+1), solve(node.right, level+1))
        if d == 1:
            return TreeNode(v, solve(root), None)
        return solve(root)
