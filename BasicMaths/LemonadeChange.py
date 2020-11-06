class Solution:
    def lemonadeChange(self, bills) -> bool:
        fives = 0
        tens = 0
        twens = 0
        for b in bills:
            if b == 5:
                fives += 1
            elif b == 10:
                tens += 1
                if fives < 1:
                    return False
                fives -= 1
            else:
                twens += 1
                if tens > 0:
                    tens -= 1
                    if fives < 1:
                        return False
                    else:
                        fives -= 1
                else:
                    if fives < 3:
                        return False
                    fives -= 3
        return True
