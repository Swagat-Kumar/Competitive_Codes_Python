class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        start = points[0]
        time = 0
        for i in range(1, len(points)):
            end = points[i]
            xdiff = abs(end[0]-start[0])
            ydiff = abs(end[1]-start[1])
            minn = min(xdiff, ydiff)
            xdiff -= minn
            ydiff -= minn
            time += minn
            if xdiff == 0:
                time += ydiff
            else:
                time += xdiff
            start = points[i]
        return time
