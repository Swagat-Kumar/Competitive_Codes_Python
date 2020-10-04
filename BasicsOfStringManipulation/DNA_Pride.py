t = int(input())
ans = []
dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
for i in range(t):
    n = int(input())
    dna = input()
    a = ''
    for d in dna:
        if(d == 'U'):
            a = "Error RNA nucleobases found!"
            break
        else:
            a += dict[d]
    ans.append(a)
for a in ans:
    print(a)
