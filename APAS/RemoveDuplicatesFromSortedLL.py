# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        d = {}
        aux = head
        while aux != None:
            if aux.val not in d:
                d[aux.val] = 1
            else:
                d[aux.val] += 1
            aux = aux.next
        ans = ListNode()
        aux = ans
        while head != None:
            if d[head.val] == 1:
                aux.next = ListNode(head.val)
                aux = aux.next
            head = head.next
        return ans.next
