class Solution:
    def countAndSay(self, n: int) -> str:
        def countSay(aux='1', step=1):
            if step == n:
                return aux
            recent = aux[0]
            tem = ''
            count = 0
            for i in range(len(aux)):
                if recent == aux[i]:
                    count += 1
                else:
                    tem += str(count)+recent
                    recent = aux[i]
                    count = 1
            tem += str(count)+recent
            return countSay(tem, step+1)
        return countSay()
