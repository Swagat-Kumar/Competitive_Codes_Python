t = int(input())
ans = []
for i in range(t):
    line = input().split()
    length = len(line)
    if len(line) % 2 == 0:
        mid = len(line)//2-1
    else:
        mid = len(line)//2
    st = ''
    high = len(line)-1
    for i in range(mid+1):
        st += line[high]+' '
        high -= 1
    if len(line) % 2 == 0:
        mad = mid
    else:
        mad = mid-1
    for i in range(mid+1, len(line)):
        st += line[mad]+' '
        mad -= 1
    st.rstrip()
    ans.append(st)
for a in ans:
    print(a)
