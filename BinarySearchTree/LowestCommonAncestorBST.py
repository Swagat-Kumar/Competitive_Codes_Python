# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lcs(root, p, q):
            if root.val == p.val or root.val == q.val:
                return root
            pR = p.val < root.val
            qR = q.val < root.val
            if pR and not qR:
                return root
            if not pR and qR:
                return root
            if pR and qR:
                return lcs(root.left, p, q)
            if not pR and not qR:
                return lcs(root.right, p, q)
        return lcs(root, p, q)
