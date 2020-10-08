class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        aux = [False]*len(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies >= maximum:
                aux[i] = True
        return aux
