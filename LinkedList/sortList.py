# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        listA = []
        while head != None:
            listA.append(head.val)
            head = head.next
        listA.sort()
        aux = None
        while len(listA) > 0:
            aux = ListNode(listA.pop(), aux)
        return aux
