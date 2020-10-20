# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def rangeSum(node):
            if node == None:
                return 0
            if node.val > R:
                return rangeSum(node.left)
            elif node.val < L:
                return rangeSum(node.right)
            else:
                return node.val+rangeSum(node.left)+rangeSum(node.right)
        return rangeSum(root)
