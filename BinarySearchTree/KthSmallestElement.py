# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.ans = None
        self.i = 0

        def visit(node):
            if node == None:
                return
            if self.i > k:
                return
            visit(node.left)
            self.i += 1
            if self.i == k:
                self.ans = node.val
                return
            visit(node.right)
        visit(root)
        return self.ans
