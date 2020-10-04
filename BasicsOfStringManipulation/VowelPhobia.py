t = int(input())
ans = []
dic = ['a', 'e', 'i', 'o', 'u']
for i in range(t):
    line = input()
    c = 0
    for letter in line:
        if(letter in dic):
            c += 1
    ans.append(c)
for a in ans:
    print(a)
