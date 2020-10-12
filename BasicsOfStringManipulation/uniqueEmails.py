class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniques = []
        for mail in emails:
            aux = ''
            i = 0
            notAdd = False
            while mail[i] != '@':
                if mail[i] == '.':
                    i += 1
                elif mail[i] == '+':
                    notAdd = True
                    i += 1
                elif not notAdd:
                    aux += mail[i]
                    i += 1
                else:
                    i += 1
            aux += mail[i:]
            if aux not in uniques:
                uniques.append(aux)
        return len(uniques)
