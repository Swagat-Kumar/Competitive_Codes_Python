# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        ans = ListNode()
        aux = ans
        temp = head
        while temp != None:
            if temp.val < x:
                aux.next = ListNode(temp.val)
                aux = aux.next
            temp = temp.next
        temp = head
        while temp != None:
            if temp.val >= x:
                aux.next = ListNode(temp.val)
                aux = aux.next
            temp = temp.next
        return ans.next
