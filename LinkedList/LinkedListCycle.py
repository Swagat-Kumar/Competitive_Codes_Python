# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        fast = head
        slow = head
        while fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == None:
                break
            if slow == fast and slow != None and fast != None:
                return True
        return False
