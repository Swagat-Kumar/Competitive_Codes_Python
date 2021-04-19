# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count = 0
        nextHead = head
        while nextHead != None and count < k:
            nextHead = nextHead.next
            count += 1
        if count != k:
            return head
        remaining = self.reverseKGroup(nextHead, k)
        for i in range(k):
            temp = head.next
            head.next = remaining
            remaining = head
            head = temp
        return remaining
