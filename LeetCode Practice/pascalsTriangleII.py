class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        start = 0
        listA = [1]
        while rowIndex != start:
            aux = []
            aux.append(1)
            for i in range(len(listA)-1):
                aux.append(listA[i]+listA[i+1])
            aux.append(1)
            listA = aux
            start += 1
        return listA
