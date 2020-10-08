# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def checkEquality(A, B):
            if A == None or B == None:
                if A == None and B != None:
                    return False
                if B == None and A != None:
                    return False
                return True
            if A.val != B.val:
                return False
            return checkEquality(A.left, B.left) and checkEquality(A.right, B.right)
        return checkEquality(p, q)
