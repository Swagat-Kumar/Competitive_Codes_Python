# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return None
        remove = head
        prev = None
        while remove != None:
            if remove.val == val:
                while remove.val == val:
                    remove = remove.next
                    if remove == None:
                        break
                if prev == None:
                    head = remove
                else:
                    prev.next = remove
            prev = remove
            if remove == None:
                break
            remove = remove.next
        return head
