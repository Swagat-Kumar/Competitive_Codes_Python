# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def sumR(root, s):
            if root == None:
                return 0
            if root.left == None and root.right == None:
                s += str(root.val)
                return int(s, 2)
            ss = s+str(root.val)
            return sumR(root.left, ss)+sumR(root.right, ss)
        return sumR(root, '')
