# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.minn = 0

        def visit(node, low, high):
            if node == None:
                return
            if abs(node.val-low) > self.minn:
                self.minn = abs(node.val-low)
            if node.val < low:
                low = node.val
            if abs(node.val-high) > self.minn:
                self.minn = abs(node.val-high)
            if node.val > high:
                high = node.val
            visit(node.left, low, high)
            visit(node.right, low, high)
        visit(root, root.val, root.val)
        return self.minn
