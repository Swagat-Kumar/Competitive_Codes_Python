# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        def visit(node):
            if node == None:
                return None
            leftt = visit(node.left)
            rightt = visit(node.right)
            if node.val == target and leftt == None and rightt == None:
                return None
            else:
                return TreeNode(node.val, leftt, rightt)
        return visit(root)
