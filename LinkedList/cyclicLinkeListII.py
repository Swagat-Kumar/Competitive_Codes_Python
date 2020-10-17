# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        cyclic = False
        while slow != None:
            slow = slow.next
            if fast.next == None:
                break
            fast = fast.next.next
            if slow == fast:
                cyclic = True
                slow = head
                break
            if fast == None:
                break
        if not cyclic:
            return None
        else:
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
