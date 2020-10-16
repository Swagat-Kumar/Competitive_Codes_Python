# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        def getLength(node):
            count = 0
            aux = None
            while node != None:
                aux = ListNode(node.val, aux)
                node = node.next
                count += 1
            return (count, aux)
        rootL = getLength(root)
        rootLen = rootL[0]
        iL = rootLen//k
        remainder = rootLen % k
        ans = []
        aux = rootL[1]
        for i in range(k):
            temp = None
            if (k-i) <= remainder:
                c = 1
            else:
                c = 0
            for j in range(iL+c):
                temp = ListNode(aux.val, temp)
                aux = aux.next
            ans.append(temp)
            if aux == None:
                ans = ans[::-1]
                for l in range(i+1, k):
                    ans.append(None)
                break
        return ans
