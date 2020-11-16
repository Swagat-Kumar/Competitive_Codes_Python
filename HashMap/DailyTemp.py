class Solution:
    def dailyTemperatures(self, T):
        listA = [0]*len(T)
        greater = []
        for i in range(len(T)-1, -1, -1):
            if len(greater) != 0:
                while len(greater) != 0 and greater[-1][0] <= T[i]:
                    greater.pop()
                    if len(greater) == 0:
                        break
            if len(greater) != 0:
                listA[i] = greater[-1][1]-i
            else:
                listA[i] = 0
            greater.append((T[i], i))
        return listA
