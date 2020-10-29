n = int(input())
ai = list(map(int, input().split()))
freq = {}
for a in ai:
    if a not in freq:
        freq[a] = 1
    else:
        freq[a] += 1
for i in sorted(freq):
    print(i, freq[i])
