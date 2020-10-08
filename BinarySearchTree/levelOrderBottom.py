# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        listA = []
        roots = [root]
        while len(roots) > 0:
            temp = []
            aux = []
            for r in roots:
                temp.append(r.val)
                if r.left != None:
                    aux.append(r.left)
                if r.right != None:
                    aux.append(r.right)
            listA.append(temp)
            roots = aux
        return listA[::-1]
