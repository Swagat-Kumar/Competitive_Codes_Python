class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        listA = []
        for p in paths:
            listA.append(p[0])
        for p in paths:
            if p[1] not in listA:
                return p[1]
