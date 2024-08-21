from typing import List

MOD = 10 ** 9 + 7


class Solution:

    # 暴力解 超时
    def countOfPairs(self, nums: List[int]) -> int:
        return self.dfs(nums, 0, -1, 50)

    def dfs(self, nums, n, last_a, last_b):
        if n == len(nums):
            return 1

        res = 0
        for num in range(nums[n] + 1):
            if num >= last_a and nums[n] - num <= last_b:
                res += self.dfs(nums, n + 1, num, nums[n] - num) % MOD
                res %= MOD
        return res

