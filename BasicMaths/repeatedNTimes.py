class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        aux = []
        for a in A:
            if a in aux:
                return a
            else:
                aux.append(a)
