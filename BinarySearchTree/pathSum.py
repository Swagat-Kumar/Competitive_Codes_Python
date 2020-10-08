# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False

        def solve(node, tot=0):
            if node == None:
                return False
            tot += node.val
            if node.left == None and node.right == None:
                if tot == sum:
                    return True
                else:
                    return False
            return solve(node.left, tot) or solve(node.right, tot)
        return solve(root)
