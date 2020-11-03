# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.p = 0

        def visit(imin=0, imax=len(inorder)-1):
            if imax < imin:
                return None
            preOrder = preorder[self.p]
            for j in range(imin, imax+1):
                if inorder[j] == preOrder:
                    self.p += 1
                    return TreeNode(preOrder, visit(imin, j-1), visit(j+1, imax))
            return None
        return visit()
