# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        aux = None
        while head != None:
            temp = ListNode(head.val, aux)
            aux = temp
            head = head.next
        return aux
