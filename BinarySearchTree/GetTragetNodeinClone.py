# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def getTargetCopy(self, original, cloned, target):
        self.ans = None

        def visit(node):
            if node == None:
                return
            if node.val == target.val:
                self.ans = node
                return
            visit(node.left)
            if self.ans != None:
                return
            visit(node.right)
        visit(cloned)
        return self.ans
