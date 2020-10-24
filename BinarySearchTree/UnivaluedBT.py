# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        self.value = root.val

        def visit(node):
            if node == None:
                return True
            if node.val != self.value:
                return False
            return visit(node.left) and visit(node.right)
        return visit(root)
