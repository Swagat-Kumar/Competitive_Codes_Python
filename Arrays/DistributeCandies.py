class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        x = 1
        array = [0]*num_people
        i = 0
        while x <= candies:
            array[i] += x
            candies -= x
            x += 1
            i += 1
            if i == num_people:
                i = 0
        if candies != 0:
            array[i] += candies
        return array
