# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        def depth(node):
            if node == None:
                return 0
            return 1+max(depth(node.left), depth(node.right))
        listA = [0]*(depth(root)+1)

        def summ(node, current=1):
            if node == None:
                return None
            listA[current] += node.val
            summ(node.left, current+1)
            summ(node.right, current+1)
        summ(root)
        print(listA)
        maxx = 1
        for j in range(1, len(listA)):
            if listA[j] > listA[maxx]:
                maxx = j
        return maxx
