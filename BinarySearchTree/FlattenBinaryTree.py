# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        listA = []

        def visit(node):
            if node == None:
                return
            listA.append(node.val)
            visit(node.left)
            visit(node.right)
        visit(root)
        pointer = root
        for j in range(len(listA)):
            pointer.val = listA[j]
            pointer.left = None
            if j == len(listA)-1:
                break
            if pointer.right == None:
                pointer.right = TreeNode(0)
            pointer = pointer.right
