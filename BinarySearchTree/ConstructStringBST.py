# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def tree2str(self, t: TreeNode) -> str:
        def visit(node):
            if node == None:
                return ''
            aux = str(node.val)
            a = '('+visit(node.left)+')'
            b = '('+visit(node.right)+')'
            if a == b == '()':
                return aux
            if b == '()' and a != '()':
                return aux+a
            return aux+a+b
        return visit(t)
