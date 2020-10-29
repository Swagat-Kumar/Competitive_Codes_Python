# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        dicA = {}
        self.maxF = 0

        def visit(node):
            if node == None:
                return
            visit(node.left)
            if node.val not in dicA:
                dicA[node.val] = 1
                if 1 > self.maxF:
                    self.maxF = 1
            else:
                dicA[node.val] += 1
                if dicA[node.val] > self.maxF:
                    self.maxF = dicA[node.val]
            visit(node.right)
        visit(root)
        listA = []
        for d in dicA:
            if dicA[d] == self.maxF:
                listA.append(d)
        return listA
