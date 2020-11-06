# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isCousins(self, root, x: int, y: int) -> bool:
        self.xx = -1
        self.parentx = -1
        self.parenty = -1
        self.yy = -1

        def visit(node, level=0, parent=None):
            if node == None:
                return
            if node.val == x:
                self.xx = level
                self.parentx = parent
            elif node.val == y:
                self.yy = level
                self.parenty = parent
            visit(node.left, level+1, node.val)
            visit(node.right, level+1, node.val)
        visit(root)
        return self.xx == self.yy and self.parentx != self.parenty
