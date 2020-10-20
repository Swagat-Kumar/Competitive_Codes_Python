class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sumA = 0
        product = 1
        nn = n+0
        while nn != 0:
            sumA += (nn % 10)
            product *= (nn % 10)
            nn = nn//10
        return product-sumA
