import bisect
n = int(input())
ai = list(map(int, input().split()))
ai.sort()
score = 0

for i in range(1, len(ai)+1):
    score += bisect.bisect_left(ai, ai[-i])
print(score)
