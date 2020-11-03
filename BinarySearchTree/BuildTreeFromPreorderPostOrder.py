# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def visit(p=0, imin=0, imax=len(inorder)-1):
            if p >= len(preorder) or imax < imin:
                return None
            for pp in range(p, len(preorder)):
                for j in range(imin, imax+1):
                    if preorder[pp] == inorder[j]:
                        return TreeNode(preorder[pp], visit(p+1, imin, j-1), visit(p+1, j+1, imax))
            return None
        return visit()
