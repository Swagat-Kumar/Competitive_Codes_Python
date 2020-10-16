# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def addTo(low, high):
            if high < low:
                return None
            if high == low:
                return TreeNode(nums[low])
            mid = (low+high)//2
            return TreeNode(nums[mid], addTo(low, mid-1), addTo(mid+1, high))
        return addTo(0, len(nums)-1)
