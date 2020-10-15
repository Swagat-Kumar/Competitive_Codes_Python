# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        def getReverse(node):
            aux = None
            count = 0
            while node != None:
                aux = ListNode(node.val, aux)
                node = node.next
                count += 1
            return (aux, count)
        revv = getReverse(head)
        rev = revv[0]
        l = revv[1]
        ans = None
        if l == 0:
            return head
        if l % 2 == 0:
            firstPass = rev
            secondPass = rev.next
        else:
            firstPass = rev.next
            secondPass = rev
        aux = firstPass
        while aux != None:
            ans = ListNode(aux.val, ans)
            if aux.next == None:
                break
            aux = aux.next.next
        aux = secondPass
        while aux != None:
            ans = ListNode(aux.val, ans)
            if aux.next == None:
                break
            aux = aux.next.next
        return ans
