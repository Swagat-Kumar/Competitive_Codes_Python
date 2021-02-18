class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort()
        self.aux = nums

    def add(self, val: int) -> int:
        if len(self.aux) == 0:
            self.aux = [val]
        else:
            lo = 0
            hi = len(self.aux)-1
            mid = 0
            while lo <= hi:
                mid = (lo+hi)//2
                if val >= self.aux[mid]:
                    lo = mid+1
                else:
                    hi = mid-1
            while self.aux[mid] < val:
                mid += 1
                if mid >= len(self.aux)-1:
                    break

            self.aux = self.aux[:mid]+[val]+self.aux[mid:]
        return self.aux[len(self.aux)-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
