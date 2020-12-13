t = int(input())
number_inputs = ''
for i in range(t):
    number_inputs += str(input())+','
number_inputs = number_inputs[0:len(number_inputs)-1]
number_array = number_inputs.split(',')
c = 0
for number in number_array:
    if(int(number) % 21 == 0):
        print('The streak is broken!')
        continue
    c = 0
    for index in range(len(number)-1):
        if(number[index:index+2] == '21'):
            print('The streak is broken!')
            c = 1
            break
    if(c):
        continue
    print('The streak lives still in our heart!')
