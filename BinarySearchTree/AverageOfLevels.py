# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        listA = []
        nodes = [root]
        while len(nodes) != 0:
            aux = []
            sumA = 0
            count = 0
            for n in nodes:
                if n == None:
                    continue
                sumA += n.val
                count += 1
                if n.left != None:
                    aux.append(n.left)
                if n.right != None:
                    aux.append(n.right)
            if count == 0:
                break
            listA.append(sumA/count)
            nodes = aux
        return listA
