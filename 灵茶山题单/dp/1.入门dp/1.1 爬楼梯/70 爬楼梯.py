class Solution:
    # def climbStairs(self, n: int) -> int:
    #     cache = [-1] * (n + 1)
    #     def dfs(i):
    #         if i < 0:
    #             return 0
    #         if i == 0:
    #             return 1
    #         if cache[i] != -1:
    #             return cache[i]
    #         res = dfs(i-1) + dfs(i-2)
    #         cache[i] = res
    #         return res
    #     return dfs(n)

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        f = [0] * (n + 1)
        f0, f1 = 1, 1
        res = 0
        for i in range(2, n+1):
            res = f0 + f1
            f0 = f1
            f1 = res
        return res
