# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.sumA = 0

        def visit(node, st=''):
            if node == None:
                return
            if node.left == None and node.right == None:
                st += str(node.val)
                self.sumA += int(st)
            st += str(node.val)
            visit(node.left, st+'')
            visit(node.right, st+'')
        visit(root)
        return self.sumA
