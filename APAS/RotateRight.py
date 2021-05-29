# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        l = 0
        lenn = head
        while lenn != None:
            l += 1
            lenn = lenn.next
        if l == 0:
            return head
        k = k % l
        if k == 0:
            return head
        ans = ListNode()
        auxx = ListNode()
        aux = auxx
        fast = head
        h = head
        for i in range(k):
            fast = fast.next
        while fast != None:
            aux.next = ListNode(h.val)
            aux = aux.next
            h = h.next
            fast = fast.next
        pointer = h
        for i in range(k-1):
            pointer = pointer.next
        pointer.next = auxx.next
        return h
