# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return None
        ans = []
        nodes = [root]
        while len(nodes) != 0:
            aux = []
            for n in nodes:
                aux.append(n.val)
            ans.append(aux)
            aux = []
            for n in nodes:
                if n.left != None:
                    aux.append(n.left)
                if n.right != None:
                    aux.append(n.right)
            nodes = aux
        return ans
