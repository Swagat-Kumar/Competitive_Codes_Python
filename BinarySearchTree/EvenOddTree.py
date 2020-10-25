# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        level = 0
        nodes = [root]
        while len(nodes) != 0:
            aux = []
            if level % 2 == 0:
                if nodes[0].val % 2 == 0:
                    return False
                if nodes[0].left != None:
                    aux.append(nodes[0].left)
                if nodes[0].right != None:
                    aux.append(nodes[0].right)
                for i in range(1, len(nodes)):
                    if nodes[i].val <= nodes[i-1].val or nodes[i].val % 2 == 0:
                        return False
                    if nodes[i].left != None:
                        aux.append(nodes[i].left)
                    if nodes[i].right != None:
                        aux.append(nodes[i].right)
            else:
                if nodes[0].val % 2 != 0:
                    return False
                if nodes[0].left != None:
                    aux.append(nodes[0].left)
                if nodes[0].right != None:
                    aux.append(nodes[0].right)
                for i in range(1, len(nodes)):
                    if nodes[i].val >= nodes[i-1].val or nodes[i].val % 2 != 0:
                        return False
                    if nodes[i].left != None:
                        aux.append(nodes[i].left)
                    if nodes[i].right != None:
                        aux.append(nodes[i].right)
            nodes = aux
            level += 1
        return True
