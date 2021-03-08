# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        first = head
        ans = ListNode()
        aux = ans
        while first != None:
            if first.next == None:
                aux.next = ListNode(first.val)
                aux = aux.next
                first = None
            else:
                aux.next = ListNode(first.next.val)
                aux = aux.next
                aux.next = ListNode(first.val)
                aux = aux.next
                first = first.next.next
        return ans.next
