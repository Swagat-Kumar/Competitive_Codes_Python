class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if Y <= X:
            return abs(Y-X)
        else:
            steps = 0
            while Y > X:
                if Y % 2 == 1:
                    Y += 1
                else:
                    Y //= 2
                steps += 1
            return abs(Y-X)+steps
