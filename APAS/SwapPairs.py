# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def swap(l1, l2):
            l1.next = l2.next
            l2.next = l1
            return l2
        ans = ListNode()
        ans.next = head
        pt = ans
        while pt != None and pt.next != None and pt.next.next != None:
            pt.next = swap(pt.next, pt.next.next)
            pt = pt.next.next
        return ans.next
