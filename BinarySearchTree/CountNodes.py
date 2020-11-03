# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        self.count = 0

        def visit(node):
            if node == None:
                return
            self.count += 1
            visit(node.left)
            visit(node.right)
        visit(root)
        return self.count
