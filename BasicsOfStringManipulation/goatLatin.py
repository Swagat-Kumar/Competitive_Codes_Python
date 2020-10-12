class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        words = S.split()
        i = 1
        aux = ''
        for w in words:
            temp = ''
            if w[0] in vowel:
                temp = w+'ma'+i*'a'
            else:
                temp = w[1:]+w[0]+'ma'+i*'a'
            i += 1
            aux += temp+' '
        return aux[:len(aux)-1]
