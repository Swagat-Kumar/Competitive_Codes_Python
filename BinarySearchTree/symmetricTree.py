# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def sym(A, B):
            if A == None or B == None:
                if A == None and B == None:
                    return True
                else:
                    return False
            if A.val != B.val:
                return False
            return sym(A.left, B.right) and sym(A.right, B.left)
        if root == None:
            return True
        else:
            return sym(root.left, root.right)
