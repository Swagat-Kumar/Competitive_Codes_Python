# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        listA = []

        def visit(node):
            if node == None:
                return
            visit(node.left)
            visit(node.right)
            listA.append(node.val)
        visit(root)
        return listA
