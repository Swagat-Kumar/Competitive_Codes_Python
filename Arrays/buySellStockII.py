class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        while i < len(prices)-1:
            try:
                while prices[i+1] < prices[i]:
                    i += 1
            except:
                pass
            buy = i
            i += 1
            if i >= len(prices):
                break
            try:
                while prices[i] > prices[i-1]:
                    i += 1
            except:
                pass
            end = i-1
            profit += (prices[end]-prices[buy])
        return profit
