# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        listA = []

        def depth(node):
            if node == None:
                return 0
            return 1+max(depth(node.left), depth(node.right))
        listA = [[] for i in range(depth(root))]

        def visit(node, level=0):
            if node == None:
                return
            listA[level].append(node.val)
            visit(node.left, level+1)
            visit(node.right, level+1)
        visit(root)
        for i in range(len(listA)):
            if i % 2 != 0:
                listA[i] = listA[i][::-1]
        return listA
