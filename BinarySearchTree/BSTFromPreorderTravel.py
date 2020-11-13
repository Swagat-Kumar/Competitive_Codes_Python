# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder) -> TreeNode:
        self.i = 0

        def visit(low=0, high=10**9):
            if self.i >= len(preorder):
                return None
            x = preorder[self.i]
            if x > low and x < high:
                self.i += 1
                return TreeNode(x, visit(low, x), visit(x, high))
            else:
                return None
        return visit()
