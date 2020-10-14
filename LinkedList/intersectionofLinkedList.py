# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def getLengthTail(Node):
            l = 0
            previous = None
            while Node != None:
                previous = Node
                Node = Node.next
                l += 1
            return (l, previous)
        auxA = getLengthTail(headA)
        auxB = getLengthTail(headB)
        if auxA[1] != auxB[1]:
            return None
        longer = headA if auxA[0] > auxB[0] else headB
        short = headB if auxA[0] > auxB[0] else headA
        dif = abs(auxB[0]-auxA[0])
        for i in range(dif):
            longer = longer.next
        while longer != None and short != None:
            if longer == short:
                return longer
            longer = longer.next
            short = short.next
        return None
