# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumEvenGrandparent(self, root) -> int:
        self.sum = 0

        def visit(node, p=None, gp=None):
            if node == None:
                return
            if p == None and gp == None:
                visit(node.left, node.val, None)
                visit(node.right, node.val, None)
            else:
                if gp != None:
                    if gp % 2 == 0:
                        self.sum += node.val
                visit(node.left, node.val, p)
                visit(node.right, node.val, p)
        visit(root)
        return self.sum
