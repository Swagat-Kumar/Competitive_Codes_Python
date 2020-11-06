class Solution:
    def findRestaurant(self, list1, list2):
        currentSum = 9000
        listA = []
        dic = {}
        i = 0
        for l in list1:
            dic[l] = i
            i += 1
        print(dic)
        for i in range(len(list2)):
            if list2[i] in dic:
                if i+dic[list2[i]] < currentSum:
                    listA = []
                    currentSum = i+dic[list2[i]]
                    listA.append(list2[i])
                elif i+dic[list2[i]] == currentSum:
                    listA.append(list2[i])
        return listA
