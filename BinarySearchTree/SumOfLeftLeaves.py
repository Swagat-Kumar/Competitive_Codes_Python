# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.sum = 0
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 0

        def visit(node, left=True):
            if node == None:
                return
            if node.left == None and node.right == None:
                if left:
                    self.sum += node.val
                return
            visit(node.left, True)
            visit(node.right, False)
        visit(root, True)
        return self.sum
