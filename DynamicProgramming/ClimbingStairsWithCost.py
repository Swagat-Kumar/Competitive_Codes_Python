class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        auxC = [0]*len(cost)
        auxC[0] = cost[0]
        auxC[1] = cost[1]
        if len(cost) == 2:
            return auxC[1]
        for i in range(2, len(cost)):
            auxC[i] = cost[i]+min(auxC[i-1], auxC[i-2])
        return min(auxC[-1], auxC[-2])
