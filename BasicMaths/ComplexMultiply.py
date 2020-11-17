class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        def first(st):
            for i in range(len(st)):
                if st[i] == '+':
                    return i
        aa = first(a)
        bb = first(b)
        A = int(a[:aa])
        B = int(a[aa+1:len(a)-1])
        C = int(b[:bb])
        D = int(b[bb+1:len(b)-1])
        aux = str(A*C-B*D)+'+'+str(A*D+B*C)+'i'
        return aux
