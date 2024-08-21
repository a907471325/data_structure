from typing import List


class Solution:

    # def rob(self, nums: List[int]) -> int:
    #     # f(n) = max( f(n-1) , f(n-2) + nums[n] )
    #     cache = [-1] * (len(nums) + 1)
    #     def dfs(n):
    #         if n <= 0:
    #             return 0
    #         if cache[n] != -1:
    #             return cache[n]
    #         res = max(dfs(n-2) + nums[n-1], dfs(n-1))
    #         cache[n] = res
    #         return res
    #     return dfs(len(nums))

    def rob(self, nums: List[int]) -> int:
        # f(n) = max( f(n-1) , f(n-2) + nums[n] )
        n = len(nums)
        f = [0] * (n + 1)
        f[1] = nums[0]
        for i in range(2, len(nums)+1):
            f[i] = max(f[i-1], f[i-2] + nums[i-1])
        return f[len(nums)]