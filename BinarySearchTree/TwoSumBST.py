# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        listA = []

        def visit(node):
            if node == None:
                return
            visit(node.left)
            listA.append(node.val)
            visit(node.right)
        visit(root)
        if len(listA) <= 1:
            return False
        low = 0
        high = len(listA)-1
        while low < high:
            if listA[low]+listA[high] == k:
                return True
            if listA[low]+listA[high] > k:
                high -= 1
            else:
                low += 1
        return False
