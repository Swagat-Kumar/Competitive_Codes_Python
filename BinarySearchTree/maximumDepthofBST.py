# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def depth(A, current=0):
            if A == None:
                return current
            return max(depth(A.left, current+1), depth(A.right, current+1))

        return depth(root)
