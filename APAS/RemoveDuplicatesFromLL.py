# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ans = ListNode()
        aux = ans
        while head != None:
            if head.next != None and head.val == head.next.val:
                head = head.next
                continue
            aux.next = ListNode(head.val)
            aux = aux.next
            head = head.next

        return ans.next
