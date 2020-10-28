# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        listA = []

        def visit(node, temp=[]):
            if node == None:
                return
            if node.left == node.right == None:
                temp.append(str(node.val))
                listA.append(temp)
                return
            temp.append(str(node.val))
            visit(node.left, list(temp))
            visit(node.right, list(temp))
        visit(root)
        for i in range(len(listA)):
            aux = listA[i]
            aux = '->'.join(aux)
            listA[i] = aux
        return listA
