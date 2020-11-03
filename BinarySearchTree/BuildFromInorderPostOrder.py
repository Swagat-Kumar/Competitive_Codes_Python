# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        self.p = len(postorder)-1

        def build(imin=0, imax=len(inorder)-1):
            if imax < imin:
                return None
            num = postorder[self.p]
            for j in range(imin, imax+1):
                if num == inorder[j]:
                    self.p -= 1
                    right = build(j+1, imax)
                    left = build(imin, j-1)
                    return TreeNode(num, left, right)
            return None
        return build()
