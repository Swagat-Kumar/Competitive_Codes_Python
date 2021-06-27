# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        temp = head
        low = ListNode()
        l = low
        high = ListNode()
        h = high
        while temp != None:
            if temp.val < x:
                l.next = temp
                l = l.next
            else:
                h.next = temp
                h = h.next
            temp = temp.next
        h.next = None
        l.next = high.next
        return low.next
