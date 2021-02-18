class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def compare(a, b):
            if a < b:
                return -1
            elif a > b:
                return 1
            else:
                return 0

        def select(a, lo, hi):
            lt = lo
            gt = hi
            i = lo
            v = a[lo]
            while i <= gt:
                cmp = compare(a[i], v)
                if cmp < 0:
                    a[i], a[lt] = a[lt], a[i]
                    lt += 1
                    i += 1
                elif cmp > 0:
                    a[i], a[gt] = a[gt], a[i]
                    gt -= 1
                else:
                    i += 1
            if lt > k:
                return select(a, lo, lt-1)
            elif gt < k:
                return select(a, gt+1, hi)
            else:
                return a[lt]
        k = len(nums)-k
        return select(nums, 0, len(nums)-1)
