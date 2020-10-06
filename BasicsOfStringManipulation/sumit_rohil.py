t = int(input())
listA = []
for i in range(t):
    st = input()
    ut = ''.join(sorted(st))
    ut = ut+st[0]+st[len(st)-1]
    if ut not in listA:
        listA.append(ut)
print(len(listA))
