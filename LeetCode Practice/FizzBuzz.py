class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        listA = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                listA.append('FizzBuzz')
            elif i % 3 == 0:
                listA.append('Fizz')
            elif i % 5 == 0:
                listA.append('Buzz')
            else:
                listA.append(str(i))
        return listA
