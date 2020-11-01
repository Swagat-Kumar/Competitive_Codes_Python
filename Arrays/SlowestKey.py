class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        prev = 0
        key = ''
        maxT = -1
        for i in range(len(releaseTimes)):
            time = releaseTimes[i]-prev
            if time >= maxT:
                if time == maxT:
                    if key < keysPressed[i]:
                        maxT = time
                        key = keysPressed[i]
                else:
                    maxT = time
                    key = keysPressed[i]
            prev = releaseTimes[i]
        return key
