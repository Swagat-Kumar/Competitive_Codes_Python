# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        listA = []

        def visit(node):
            if node == None:
                return
            if node.left == None and node.right == None:
                listA.append(node.val)
            visit(node.left)
            visit(node.right)
            return listA
        visit(root1)
        A = listA
        listA = []
        visit(root2)
        B = listA
        return A == B
