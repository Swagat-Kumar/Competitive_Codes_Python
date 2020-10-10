class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = [-1]*len(prices)
        aux = []
        for i in range(len(prices)-1, -1, -1):
            if len(aux) == 0:
                ans[i] = prices[i]
            else:
                while aux[-1] > prices[i]:
                    aux.pop()
                    if len(aux) == 0:
                        break
                if len(aux) == 0:
                    ans[i] = prices[i]
                else:
                    ans[i] = prices[i]-aux[-1]
            aux.append(prices[i])
        return ans
