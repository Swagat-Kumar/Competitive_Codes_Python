# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.listA = []

        def travel(node):
            if node == None:
                return
            travel(node.left)
            self.listA.append(node.val)
            travel(node.right)
        travel(root)
        return self.listA
