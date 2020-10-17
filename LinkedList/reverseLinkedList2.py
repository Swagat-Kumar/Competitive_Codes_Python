# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        def reverse(node):
            aux = None
            count = 0
            while node != None:
                aux = ListNode(node.val, aux)
                node = node.next
                count += 1
            return (aux, count)
        revv = reverse(head)
        rev = revv[0]
        l = revv[1]
        ans = None
        for i in range(l-n):
            ans = ListNode(rev.val, ans)
            rev = rev.next
        for j in range(m-1):
            head = head.next
        for i in range(n-m+1):
            ans = ListNode(head.val, ans)
            head = head.next
            rev = rev.next
        while rev != None:
            ans = ListNode(rev.val, ans)
            rev = rev.next
        return ans
