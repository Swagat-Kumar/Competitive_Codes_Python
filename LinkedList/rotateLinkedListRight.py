# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        ans = None
        if head == None:
            return None

        def getReverse(node):
            temp = None
            c = 0
            while node != None:
                temp = ListNode(node.val, temp)
                node = node.next
                c += 1
            return (temp, c)
        auxx1 = getReverse(head)
        aux1 = auxx1[0]
        l = auxx1[1]
        k = k % l
        aux2 = aux1
        for i in range(k):
            aux1 = aux1.next
            if aux1 == None:
                break
        while aux1 != None:
            ans = ListNode(aux1.val, ans)
            aux1 = aux1.next
        for i in range(k):
            ans = ListNode(aux2.val, ans)
            aux2 = aux2.next
            if aux2 == None:
                break
        return ans
