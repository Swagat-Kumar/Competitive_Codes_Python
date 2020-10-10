class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        aux = []
        dic = [1, 0]
        for line in A:
            temp = []
            for i in range(len(line)-1, -1, -1):
                temp.append(dic[line[i]])
            aux.append(temp)
        return aux
