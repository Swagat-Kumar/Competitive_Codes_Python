class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        listA = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                 "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        aux = []
        for w in words:
            word = ''
            for l in w:
                word += listA[ord(l)-97]
            if word not in aux:
                aux.append(word)
        return len(aux)
