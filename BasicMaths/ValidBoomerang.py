class Solution:
    def isBoomerang(self, points) -> bool:
        def distance(p1, p2):
            return ((abs(p1[0]-p2[0])**2)+abs(p1[1]-p2[1])**2)**0.5
        listA = []
        for p in points:
            if p in listA:
                return False
            listA.append(p)
        d01 = distance(points[0], points[1])
        d12 = distance(points[1], points[2])
        d02 = distance(points[0], points[2])
        if d01+d12 == d02:
            return False
        if d12+d02 == d01:
            return False
        if d02+d01 == d12:
            return False
        return True
