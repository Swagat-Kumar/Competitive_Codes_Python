# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        self.ans = ''

        def visit(node, st=''):
            if node == None:
                return None
            if node.left == None and node.right == None:
                st += chr(97+node.val)
                if self.ans == '':
                    self.ans = st[::-1]
                if st[::-1] < self.ans:
                    self.ans = st[::-1]
                return
            st += chr(97+node.val)
            visit(node.left, st+'')
            visit(node.right, st+'')
        visit(root)
        return self.ans
