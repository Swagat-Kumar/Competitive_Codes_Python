s = input()
aux = [0]*len(s)
count = 0
for i in range(len(s)-1, -1, -1):
    if int(s[i]) % 2 == 0:
        count += 1
    aux[i] = count
ans = ''
for a in aux:
    ans += str(a)+' '
print(ans[:len(ans)-1])
