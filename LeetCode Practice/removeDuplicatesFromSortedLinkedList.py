# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        previous = None
        listA = []
        while head != None:
            if head.next == None:
                if previous != head.val:
                    listA.append(head.val)
                    head = head.next
                break
            if head.val == head.next.val or head.val == previous:
                previous = head.val
            else:
                previous = head.val
                listA.append(previous)
            head = head.next
        aux = None
        for a in listA[::-1]:
            temp = ListNode(a, aux)
            aux = temp
        return aux
