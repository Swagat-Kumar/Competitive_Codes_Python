class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        start = 0
        i = 0
        if name[0] != typed[0]:
            return False
        while start < len(typed):
            if i == len(name):
                i -= 1
            if typed[start] == name[i]:
                i += 1
            else:
                if typed[start] != name[i-1]:
                    return False
            start += 1
        if i == len(name):
            return True
        else:
            return False
