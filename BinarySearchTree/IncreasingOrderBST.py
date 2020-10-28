# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        listA = []

        def visit(node):
            if node == None:
                return
            visit(node.left)
            listA.append(node.val)
            visit(node.right)
        visit(root)

        def node(current=0):
            if current >= len(listA):
                return None
            return TreeNode(listA[current], None, node(current+1))
        return node()
