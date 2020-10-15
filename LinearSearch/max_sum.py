N = int(input())
integer_line = input()
integer_array = integer_line.split()
sumi = 0
n = 0
non_positive = 0
fe = 1
no_zeros = 0
for i in integer_array:
    if(int(i) <= 0):
        non_positive += 1
for i in integer_array:
    if(int(i) == 0):
        no_zeros += 1
if(non_positive != len(integer_array)):
    for i in integer_array:
        if(int(i) > 0):
            sumi += int(i)
            n += 1
    print(str(sumi)+' '+str(n+no_zeros))
else:
    for i in integer_array:
        if(fe):
            maxi = int(i)
            fe = 0
        if(int(i) > maxi):
            maxi = int(i)
    print(str(maxi)+' '+'1')
