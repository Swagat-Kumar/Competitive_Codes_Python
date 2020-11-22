# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def visit(node, ans):
            if node == None:
                return 0
            left = visit(node.left, ans)
            right = visit(node.right, ans)
            leftM = 0
            rightM = 0
            if node.left and node.left.val == node.val:
                leftM = left+1
            if node.right and node.right.val == node.val:
                rightM = right+1
            ans[0] = max(ans[0], leftM+rightM)
            return max(leftM, rightM)
        ans = [0]
        visit(root, ans)
        return ans[0]
