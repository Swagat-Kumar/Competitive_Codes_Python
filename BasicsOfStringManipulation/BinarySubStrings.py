class Solution:
    def queryString(self, S: str, N: int) -> bool:
        for i in range(1, N+1):
            binary = bin(i).replace('0b', '')
            if S.find(binary) < 0:
                return False
        return True
