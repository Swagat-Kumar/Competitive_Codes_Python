'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t = int(input())
ans = []
for i in range(t):
    n, m = map(int, input().split())
    line = input()
    st = ''
    for s in line:
        x = ord(s)
        if s.islower():
            x = x-96+m
            x %= 26
            if x == 0:
                x = 26
            st += chr(96+x)
            continue
        if s.isupper():
            x = x-64+m
            x %= 26
            if x == 0:
                x = 26
            st += chr(64+x)
            continue
        if s.isdigit():
            x = (x-48+m) % 10+48
            st += chr(x)
            continue
        st += s
    print(st)
