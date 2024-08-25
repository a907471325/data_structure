from typing import List


class Solution:
    # def combinationSum4(self, nums: List[int], target: int) -> int:

    #     n = len(nums)
    #     cache = [-1] * (target + 1)
    #     def dfs(s):
    #         if s < 0:
    #             return 0
    #         if s == 0:
    #             return 1
    #         if cache[s] != -1:
    #             return cache[s]
    #         res = 0
    #         for i in nums:
    #             res += dfs(s-i)
    #         cache[s] = res
    #         return res
    # return dfs(target)

    def combinationSum4(self, nums: List[int], target: int) -> int:

        n = len(nums)
        f = [0] * (target + 1)
        f[0] = 1
        for i in range(1, target + 1):
            for x in nums:
                if x <= i:
                    f[i] += f[i - x]

        return f[target]