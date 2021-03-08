# Definition for singly-linked list.
from queue import PriorityQueue as pq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists) -> ListNode:
        Q = pq()
        for l in lists:
            while l != None:
                Q.put(l.val)
                l = l.next
        ans = ListNode()
        first = ans
        while not Q.empty():
            l = Q.get()
            first.next = ListNode(l)
            first = first.next
        return ans.next
