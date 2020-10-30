from queue import PriorityQueue
q = PriorityQueue()
t = int(input())
ans = []
for i in range(t):
    x = int(input())
    q.put((-x, x))
    if(i < 2):
        ans.append(-1)
    else:
        first = q.get()[1]
        second = q.get()[1]
        third = q.get()[1]
        q.put((-first, first))
        q.put((-second, second))
        q.put((-third, third))
        ans.append(str(first)+" "+str(second)+" "+str(third))
for a in ans:
    print(a)
