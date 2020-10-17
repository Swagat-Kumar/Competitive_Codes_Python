# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        def getReverse(node):
            aux = None
            while node != None:
                aux = ListNode(node.val, aux)
                node = node.next
            return aux
        revv = getReverse(head)
        ans = None
        less = revv
        greater = revv
        while greater != None:
            if greater.val >= x:
                ans = ListNode(greater.val, ans)
            greater = greater.next
        while less != None:
            if less.val < x:
                ans = ListNode(less.val, ans)
            less = less.next
        return ans
