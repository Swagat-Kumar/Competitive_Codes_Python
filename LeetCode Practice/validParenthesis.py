class Solution:
    def isValid(self, s: str) -> bool:
        listA = []
        left = '({['
        right = ']})'
        good = True
        for c in s:
            if c in left:
                listA.append(c)
                continue
            if c in right:
                try:
                    z = listA.pop(len(listA)-1)
                    if c == ')' and z == '(':
                        continue
                    if c == ']' and z == '[':
                        continue
                    if c == '}' and z == '{':
                        continue
                    good = False
                    break
                except:
                    return False
        print(listA)
        return len(listA) == 0 and good
