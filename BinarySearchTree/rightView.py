# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        listA = []
        self.level = -1

        def visit(node, level=0):
            if node == None:
                return
            if level > self.level:
                listA.append(node.val)
                self.level += 1
            visit(node.right, level+1)
            visit(node.left, level+1)
        visit(root)
        return listA
