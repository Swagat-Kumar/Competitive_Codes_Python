class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        listA = [[1]]
        j = 0
        while len(listA) != numRows:
            aux = []
            aux.append(1)
            for i in range(len(listA[j])-1):
                aux.append(listA[j][i]+listA[j][i+1])
            aux.append(1)
            j += 1
            listA.append(aux)
        return listA
