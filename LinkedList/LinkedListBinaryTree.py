# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        aux = []
        while head != None:
            aux.append(head.val)
            head = head.next

        def addTo(low, high):
            if high < low:
                return None
            if high == low:
                return TreeNode(aux[low])
            mid = (low+high)//2
            return TreeNode(aux[mid], addTo(low, mid-1), addTo(mid+1, high))
        return addTo(0, len(aux)-1)
