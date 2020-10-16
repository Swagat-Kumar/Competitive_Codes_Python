target = int(input())
array = list(map(int, input().split()))
array.sort()
print(array)
for i in range(len(array)-1):
    begin = i+1
    end = len(array)-1
    while begin != end and begin < len(array) and end > 0:
        if array[begin]+array[end]+array[i] == target:
            print(array[i], array[begin], array[end])
            begin += 1
            continue
        if array[begin]+array[end]+array[i] > target:
            end -= 1
        if array[begin]+array[end]+array[i] < target:
            begin += 1
