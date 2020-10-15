n_lines = int(input())
max_weight = -1
sum_lines = ''
weight_array = ''
for i in range(n_lines):
    sum_lines += input()+','
sum_lines = sum_lines[0:len(sum_lines)-1]
message_array = sum_lines.split(',')
for date in range(1, 31):
    weight = 0
    for line in message_array:
        words = line.split()
        for compare in words:
            if(compare == str(date)):
                if(words[0] == 'G:'):
                    weight += 2
                elif (words[0] == 'M:'):
                    weight += 1
    weight_array += str(weight)+','
weight_array = weight_array[0:len(weight_array)-1]
ans_array = weight_array.split(',')
for i in range(0, 30):
    if((int(ans_array[i]) == max_weight) and (int(ans_array[i]) != 0)):
        Date = 90
        break
    if(int(ans_array[i]) > max_weight):
        Date = i+1
        max_weight = int(ans_array[i])
if(Date == 19 or Date == 20):
    print('Date')
else:
    print('No Date')
