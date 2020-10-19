class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        aux = ['']*len(s)
        for i in range(len(s)):
            aux[indices[i]] = s[i]
        return ''.join(aux)
