# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        listA = []

        def visit(node):
            if node == None:
                return
            visit(node.left)
            listA.append(node.val)
            visit(node.right)
        visit(root)
        if len(listA) == 2:
            return listA[1]-listA[0]
        if len(listA) < 2:
            return 2147483647
        minD = 2147483647
        for i in range(1, len(listA)):
            if listA[i]-listA[i-1] < minD:
                minD = listA[i]-listA[i-1]
        return minD
