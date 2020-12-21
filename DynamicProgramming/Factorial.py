'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t = int(input())


def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


def factorial(n):
    if n <= 1:
        return 1
    else:
        return factorial(n-1)*n % (10**9+7)


factorial = memoize(factorial)
for i in range(t):
    n = int(input())
    print(factorial(n))
