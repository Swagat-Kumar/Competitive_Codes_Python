# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.sumA = 0
        self.maxL = 0

        def visit(node, l=0):
            if node == None:
                return
            if node.left == None and node.right == None:
                if l > self.maxL:
                    self.sumA = node.val
                    self.maxL = l
                elif l == self.maxL:
                    self.sumA += node.val
            visit(node.left, l+1)
            visit(node.right, l+1)
        visit(root)
        return self.sumA
