class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        if flowerbed == None or len(flowerbed) == 0:
            return False
        aux = 0
        count = 1
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                count += 1
            else:
                aux += (count-1)//2
                count = 0
        if count != 0:
            aux += count//2
        return aux >= n
