# code
from queue import PriorityQueue as pq
t = int(input())
mini = pq()
maxi = pq()
x = int(input())
mini.put(-1*x)
avg = x
print(x)
for tt in range(t-1):
    x = int(input())
    if mini.qsize() > maxi.qsize():
        if x < avg:
            maxi.put(-1*mini.get())
            mini.put(-1*x)
        else:
            maxi.put(x)
        mm = maxi.get()
        nn = mini.get()
        avg = (mm+nn*-1)//2
        mini.put(nn)
        maxi.put(mm)
    elif mini.qsize() == maxi.qsize():
        if x < avg:
            mini.put(-1*x)
            yy = mini.get()
            avg = yy*-1
            mini.put(yy)
        else:
            maxi.put(x)
            yy = maxi.get()
            avg = yy
            maxi.put(yy)
    else:
        if x > avg:
            mini.put(maxi.get()*-1)
            maxi.put(x)
        else:
            mini.put(-1*x)
        mm = maxi.get()
        nn = mini.get()
        avg = (mm+nn*-1)//2
        mini.put(nn)
        maxi.put(mm)
    print(avg)
