from collections import Counter
from typing import List

class Solution:

    # # n*logn 排序 + 记忆化搜索
    # def deleteAndEarn(self, nums: List[int]) -> int:

    #     nums = sorted(nums)
    #     c = Counter(nums)
    #     uniq_nums = list(c.keys())

    #     cache = [-1] * (len(uniq_nums) + 1)
    #     def dfs(n):
    #         if n <= 0:
    #             return 0
    #         if cache[n] != -1:
    #             return cache[n]
    #         res = 0
    #         use_cur = 0
    #         if uniq_nums[n-1] - uniq_nums[n-2] == 1:
    #             use_cur = uniq_nums[n-1] * c[uniq_nums[n-1]] + dfs(n-2)
    #         else:
    #             use_cur = uniq_nums[n-1] * c[uniq_nums[n-1]] + dfs(n-1)

    #         not_use = dfs(n-1)
    #         res = max(use_cur, not_use)
    #         cache[n] = res
    #         return res
    #     return dfs(len(uniq_nums))

    # 经典house robber
    def deleteAndEarn(self, nums: List[int]) -> int:
        houses = [0] * (max(nums) + 1)
        for val in nums:
            houses[val] += val
        f = [0] * (len(houses) + 1)
        f[1] = houses[0]
        for i in range(2, len(houses) + 1):
            f[i] = max(f[i - 2] + houses[i - 1], f[i - 1])
        return f[len(houses)]


if __name__ == '__main__':
    s = [1,2,3,4,9,5]
    s = sorted(s)
    c = Counter(s)

    print(s)
    print(list(c.keys()))
