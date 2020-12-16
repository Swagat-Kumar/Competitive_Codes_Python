line_input = input()
input_array = line_input.split()
X = int(input_array[0])
Y = int(input_array[1])
s = int(input_array[2])
T = int(input_array[3])
t_remaining = T-X-Y
n = 0
for i in range(0, s+1):
    for j in range(0, s+1):
        if((i+j) <= t_remaining):
            n += 1
print(n)
