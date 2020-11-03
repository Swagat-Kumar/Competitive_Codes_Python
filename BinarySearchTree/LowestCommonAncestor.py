# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def contains(a, b):
            if a == None:
                return False
            if a == b:
                return True
            if contains(a.left, b):
                return True
            if contains(a.right, b):
                return True
            return False

        def lcs(root, p, q):
            pl = contains(root.left, p)
            qr = contains(root.right, q)
            if pl and qr:
                return root
            pr = contains(root.right, p)
            ql = contains(root.left, q)
            if ql and pr:
                return root
            if pl and ql:
                return lcs(root.left, p, q)
            if pr and qr:
                return lcs(root.right, p, q)
        if contains(p, q):
            return p
        if contains(q, p):
            return q
        return lcs(root, p, q)
