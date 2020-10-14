# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        if slow == None:
            return None
        fast = head
        if fast.next == None:
            return slow
        while fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if fast == None or fast.next == None:
                return slow
        return None
