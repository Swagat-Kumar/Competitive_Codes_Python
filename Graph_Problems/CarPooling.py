class Solution:
    def carPooling(self, trips, capacity: int) -> bool:
        minn = 2000
        for t in trips:
            if t[1] < minn:
                minn = t[1]
        maxx = 0
        for t in trips:
            if t[2] > maxx:
                maxx = t[2]
        aux = [0]*(maxx-minn+1)
        for t in trips:
            for j in range(t[1], t[2]):
                aux[j-minn] += t[0]
            if max(aux) > capacity:
                return False
        return True
