N = int(input())
numbers = input()
num_array = numbers.split()
K = int(input())
for index in range(len(num_array)):
    if(num_array[index] == str(K)):
        print(index)
        break
