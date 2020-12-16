from collections import Counter
N = int(input())
string_a = input()
Array_a = list(map(int, string_a.split()))
Diction = Counter(Array_a)
Keys = list(Diction.keys())
Values = list(Diction.values())
K = int(input())
probable_ans = []
for i in range(len(Values)):
    if(Values[i] == K):
        probable_ans.append(Keys[i])
print(min(probable_ans))
