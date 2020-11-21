# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        listA = []

        def visit(node):
            if node == None:
                return
            visit(node.left)
            if node.val not in listA:
                if len(listA) < 2:
                    listA.append(node.val)
                else:
                    maxx = 0 if listA[0] > listA[1] else 1
                    if node.val < listA[maxx]:
                        del listA[maxx]
                        listA.append(node.val)
            visit(node.right)
        visit(root)
        if len(listA) < 2:
            return -1
        return max(listA)
