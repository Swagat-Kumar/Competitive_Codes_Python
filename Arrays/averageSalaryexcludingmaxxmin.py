class Solution:
    def average(self, salary: List[int]) -> float:
        minn = 10**7
        maxx = 10
        Total = 0
        for s in salary:
            if s > maxx:
                maxx = s
            if s < minn:
                minn = s
            Total += s
        Total = Total-minn-maxx
        return Total/(len(salary)-2)
