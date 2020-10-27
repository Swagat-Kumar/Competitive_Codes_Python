# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        listE = []

        def visit(node):
            if node == None:
                return
            listE.append(node.val)
            visit(node.left)
            visit(node.right)
        visit(root)
        listE.sort()

        def balance(low, high):
            if high < low:
                return None
            mid = (low+high)//2
            return TreeNode(listE[mid], balance(low, mid-1), balance(mid+1, high))
        return balance(0, len(listE)-1)
