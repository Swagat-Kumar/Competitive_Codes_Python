# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.count = 0

        def visit(node, runSum=0, aux=[]):
            if node == None:
                return
            runSum += node.val
            if runSum == sum:
                self.count += 1
            for i in range(len(aux)):
                if aux[i] == runSum-sum:
                    self.count += 1
            aux.append(runSum)
            visit(node.left, runSum, aux)
            visit(node.right, runSum, aux)
            aux.pop()
        visit(root)
        return self.count
