# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        listA = []
        while head != None:
            listA.append(head.val)
            head = head.next
        stac = []
        ans = [0]*len(listA)
        for i in range(len(listA)-1, -1, -1):
            while len(stac) > 0:
                if stac[-1] > listA[i]:
                    break
                stac.pop()
            if len(stac) > 0:
                ans[i] = stac[-1]
            else:
                ans[i] = 0
            stac.append(listA[i])
        return ans
