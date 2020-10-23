# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        root = None

        def merge(A, B):
            if A != None and B != None:
                return TreeNode(A.val+B.val, merge(A.left, B.left), merge(A.right, B.right))
            elif A == None and B != None:
                return TreeNode(B.val, merge(None, B.left), merge(None, B.right))
            elif A != None and B == None:
                return TreeNode(A.val, merge(A.left, None), merge(A.right, None))
            else:
                return None
        return merge(t1, t2)
