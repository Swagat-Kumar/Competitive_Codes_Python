# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        listA = []

        def visit(node, path=[], sumA=0):
            if node == None:
                return
            if node.left == None and node.right == None:
                path.append(node.val)
                sumA += node.val
                if sumA == sum:
                    listA.append(path)
                return
            path.append(node.val)
            sumA += node.val
            visit(node.left, list(path), sumA+0)
            visit(node.right, list(path), sumA+0)
        visit(root)
        return listA
