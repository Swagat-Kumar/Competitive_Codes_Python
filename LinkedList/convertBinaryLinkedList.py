# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        l = 0
        temp = head
        while temp != None:
            temp = temp.next
            l += 1
        l -= 1
        ans = 0
        temp = head
        while temp != None:
            ans += temp.val*(2**l)
            l -= 1
            temp = temp.next
        return ans
