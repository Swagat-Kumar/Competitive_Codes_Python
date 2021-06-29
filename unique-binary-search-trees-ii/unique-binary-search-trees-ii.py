# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generate(left,right):
            aux=[]
            if left>right:
                return [None]
            for i in range(left,right+1):
                for a in generate(left,i-1):
                    for b in generate(i+1,right):
                        aux.append(TreeNode(i,a,b))
            return aux
        return generate(1,n)
            
            
                
            
    