# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        listA = []

        def visit(node):
            if node == None:
                return
            visit(node.left)
            listA.append(node.val)
            visit(node.right)
        visit(root1)
        list1 = listA
        listA = []
        visit(root2)
        listAns = [0]*(len(listA)+len(list1))
        i = 0
        j = 0
        for k in range(len(listA)+len(list1)):
            if i >= len(list1):
                listAns[k] = listA[j]
                j += 1
            elif j >= len(listA):
                listAns[k] = list1[i]
                i += 1
            elif list1[i] < listA[j]:
                listAns[k] = list1[i]
                i += 1
            else:
                listAns[k] = listA[j]
                j += 1
        return listAns
