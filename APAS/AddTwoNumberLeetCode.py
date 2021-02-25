# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        aux = 0
        ans = None
        pointer = None
        while l1 != None or l2 != None:
            if l1 != None:
                aux += l1.val
                l1 = l1.next
            if l2 != None:
                aux += l2.val
                l2 = l2.next
            temp = ListNode(aux % 10)
            if pointer == None:
                pointer = temp
                ans = pointer
                aux = aux//10
                continue
            pointer.next = temp
            pointer = temp
            aux = aux//10
        if aux != 0:
            pointer.next = ListNode(aux)
        return ans
