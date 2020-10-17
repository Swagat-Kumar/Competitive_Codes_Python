# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def getReverseLength(node):
            aux = None
            count = 0
            while node != None:
                aux = ListNode(node.val, aux)
                node = node.next
                count += 1
            return (aux, count)
        revv = getReverseLength(head)
        rev = revv[0]
        l = revv[1]
        aux = head
        order = getReverseLength(rev)[0]
        i = 0
        while aux != None:
            if i % 2 == 0:
                aux.val = order.val
                order = order.next
            else:
                aux.val = rev.val
                rev = rev.next
            i += 1
            aux = aux.next
