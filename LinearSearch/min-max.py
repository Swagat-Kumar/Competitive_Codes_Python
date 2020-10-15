N = int(input())
integers = input()
int_array = integers.split()
fe = 1
sum = 0
for i in int_array:
    if(fe):
        min = int(i)
        max = int(i)
        fe = 0
    if(int(i) > max):
        max = int(i)
    if(int(i) < min):
        min = int(i)
    sum += int(i)
print(str(sum-max)+' '+str(sum-min))
