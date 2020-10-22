class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        key = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        ListA = []
        for s in digits:
            dList = []
            possible = key[s]
            if len(ListA) == 0:
                for p in possible:
                    dList.append(p)
                ListA = list(dList)
                continue
            for a in ListA:
                for p in possible:
                    dList.append(a+p)
            ListA = list(dList)
        return ListA
