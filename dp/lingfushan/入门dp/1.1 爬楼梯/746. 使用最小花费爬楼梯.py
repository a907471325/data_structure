from typing import List


class Solution:
    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     n = len(cost)
    #     if n == 2:
    #         return min(cost)
    #     cache = [-1] * (n+1)
    #     def dfs(i):
    #         if i == 1:
    #             return 0
    #         if i == 0:
    #             return 0
    #         if cache[i] != -1:
    #             return cache[i]
    #         res = min(dfs(i-1) + cost[i-1], dfs(i-2) + cost[i-2])
    #         cache[i] = res
    #         return res

    #     return dfs(n)

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 2:
            return min(cost)
        f0, f1 = 0, 0
        f = 0
        for i in range(2, n + 1):
            f = min(f1 + cost[i - 1], f0 + cost[i - 2])
            f0 = f1
            f1 = f

        return f


