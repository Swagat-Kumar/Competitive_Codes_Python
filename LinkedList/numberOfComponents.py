# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        idList = {}
        self.comp = len(G)
        for g in G:
            idList[g] = g

        def root(key):
            while idList[key] != key:
                key = idList[key]
            return key

        def union(A, B):
            if root(A) == root(B):
                return
            idList[A] = root(B)
            self.comp -= 1
        prev = ListNode(-1, None)
        while head != None:
            if prev.val in G and head.val in G:
                union(prev.val, head.val)
            prev = head
            head = head.next
        return self.comp
