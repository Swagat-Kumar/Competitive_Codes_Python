# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def getReverse(Node):
            aux = None
            while Node != None:
                aux = ListNode(Node.val, aux)
                Node = Node.next
            return aux
        l1R = getReverse(l1)
        l2R = getReverse(l2)
        ans = None
        carry = 0
        while l1R != None and l2R != None:
            ad = l1R.val+l2R.val+carry
            carry = ad//10
            ad = ad % 10
            ans = ListNode(ad, ans)
            l1R = l1R.next
            l2R = l2R.next
        while l1R != None:
            ad = l1R.val+carry
            carry = ad//10
            ad = ad % 10
            ans = ListNode(ad, ans)
            l1R = l1R.next
        while l2R != None:
            ad = l2R.val+carry
            carry = ad//10
            ad = ad % 10
            ans = ListNode(ad, ans)
            l2R = l2R.next
        if carry != 0:
            ans = ListNode(carry, ans)
        return ans
