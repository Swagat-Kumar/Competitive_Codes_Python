class Solution:
    def fullJustify(self, words, maxWidth: int):
        rem = maxWidth
        ans = []
        temp = []
        for w in words:
            if len(w) <= rem:
                temp.append(w)
                rem = rem-len(w)-1
            else:
                rem = maxWidth
                if len(temp) == 1:
                    ans.append(temp[0]+' '*(rem-len(temp[0])))
                    temp = [w]
                    rem = rem-len(w)-1
                else:
                    n = len(temp)
                    spaces = maxWidth
                    for t in temp:
                        spaces -= len(t)
                    div = spaces//(n-1)
                    remainSpaces = spaces % (n-1)
                    aux = ""
                    for t in range(len(temp)-1):
                        aux += temp[t]+" "*div
                        if remainSpaces > 0:
                            aux += " "
                            remainSpaces -= 1
                    aux += temp[-1]
                    ans.append(aux)
                    temp = [w]
                    rem = rem-len(w)-1
        if len(temp) != 0:
            rem = maxWidth
            aux = ''
            for t in temp:
                aux += t
                rem = rem-len(t)
                if rem > 0:
                    aux += ' '
                    rem -= 1
            aux += ' '*rem
            ans.append(aux)
        return ans
