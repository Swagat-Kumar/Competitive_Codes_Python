# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if head == None:
            return None
        dummy = ListNode(0, head)
        pre = dummy
        curr = pre.next
        while left > 1:
            pre = curr
            curr = curr.next
            left -= 1
            right -= 1
        while right > 1:
            nex = curr.next
            curr.next = nex.next
            nex.next = pre.next
            pre.next = nex
            right -= 1
        return dummy.next
