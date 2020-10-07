# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        listH = []
        while head != None:
            if head.val not in listH:
                listH.append(head.val)
            head = head.next
        aux = None
        for x in listH[::-1]:
            temp = ListNode(x, aux)
            aux = temp
        return aux
