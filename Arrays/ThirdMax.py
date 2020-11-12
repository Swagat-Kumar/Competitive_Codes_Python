class Solution:
    def thirdMax(self, nums) -> int:
        maxL = []

        def add(x):
            if x not in maxL:
                maxL.append(x)
            if len(maxL) < 4:
                return
            minx = 0
            for i in range(len(maxL)):
                if maxL[i] < maxL[minx]:
                    minx = i
            if len(maxL) > 3:
                maxL[minx], maxL[-1] = maxL[-1], maxL[minx]
                maxL.pop()
        for n in nums:
            add(n)
        if len(maxL) == 3:
            maxL.sort()
            return maxL[0]
        else:
            maxL.sort()
            return maxL[-1]
