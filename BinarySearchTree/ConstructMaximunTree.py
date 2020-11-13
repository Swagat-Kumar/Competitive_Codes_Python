# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums):
        def visit(low=0, high=len(nums)-1):
            if low > high:
                return None
            maxx = low
            for i in range(low+1, high+1):
                if nums[i] > nums[maxx]:
                    maxx = i
            return TreeNode(nums[maxx], visit(low, maxx-1), visit(maxx+1, high))
        return visit()
