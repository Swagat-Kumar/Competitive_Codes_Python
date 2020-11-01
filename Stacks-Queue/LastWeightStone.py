from queue import PriorityQueue as PQ


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = PQ()
        for s in stones:
            pq.put((-s, s))
        returned = False
        while not pq.empty():
            maxx = pq.get()[1]
            if pq.empty():
                returned = True
                break
            minn = pq.get()[1]
            if maxx != minn:
                pq.put((-maxx+minn, maxx-minn))
        if returned:
            return maxx
        else:
            return 0
