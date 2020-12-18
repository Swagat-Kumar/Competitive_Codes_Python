N = int(input())
line_input = input()
x = 0
for a in range(N-3):
    for d in range(N-1, a+2, -1):
        for b in range(a+1, d-1):
            for c in range(b+1, d):
                if(line_input[a] == line_input[c] and line_input[b] == line_input[d]):
                    x += 1
print(x)
