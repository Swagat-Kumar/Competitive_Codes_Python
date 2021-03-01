class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = x
        if n < 0 or (n != 0 and n % 10 == 0):
            return False
        else:
            x = 0
            oldNum = n+0
            while n > x:
                x = x*10+n % 10
                n = n//10
            print(n, x)
            return x == n or n == x//10
