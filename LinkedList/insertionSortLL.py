# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        ans = None
        while head != None:
            if ans == None:
                ans = ListNode(head.val)
            else:
                temp = ans
                prev = None
                while temp.val < head.val:
                    prev = temp
                    temp = temp.next
                    if temp == None:
                        break
                if prev != None:
                    prev.next = ListNode(head.val, temp)
                else:
                    ans = ListNode(head.val, temp)
            head = head.next
        return ans
