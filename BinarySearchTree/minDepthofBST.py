# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0

        def depth(node, step=1):
            if node == None:
                return 10**8
            if node.left == None and node.right == None:
                return step
            return min(depth(node.left, step+1), depth(node.right, step+1))
        return depth(root)
