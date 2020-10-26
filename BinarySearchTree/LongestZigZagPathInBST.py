# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.lp = 0

        def solve(node, path=0, prev=-1):
            if node == None:
                return
            if path > self.lp:
                self.lp = path
            if prev == -1:
                solve(node.left, 1, 0)
                solve(node.right, 1, 1)
            elif prev == 1:
                solve(node.left, path+1, 0)
                solve(node.right, 1, 1)
            else:
                solve(node.right, path+1, 1)
                solve(node.left, 1, 0)
        solve(root)
        return self.lp
