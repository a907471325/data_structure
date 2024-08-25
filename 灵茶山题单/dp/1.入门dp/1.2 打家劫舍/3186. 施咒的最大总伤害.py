from collections import Counter
from typing import List


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:

        nums = sorted(power)
        c = Counter(nums)
        uniq_nums = list(c.keys())

        prev_valid_pos = {}

        # 1 3 6 7

        # 4, 5, 6
        # 2, 4, 6
        # 2, 5, 6
        # 2, 3, 6
        # 1, 3
        for i in range(len(uniq_nums)-1, -1, -1):
            if i >= 2 and uniq_nums[i] - uniq_nums[i - 2] == 2:
                prev_valid_pos[i] = i - 3
            elif i >= 1 and uniq_nums[i] - uniq_nums[i - 1] <= 2:
                prev_valid_pos[i] = i - 2
            else:
                prev_valid_pos[i] = i - 1


        cache = [-1] * (len(uniq_nums) + 1)

        def dfs(n):
            if n <= 0:
                return 0
            if cache[n] != -1:
                return cache[n]
            res = 0
            use_cur = 0
            prev_valid_ = prev_valid_pos[n-1]

            use_cur = uniq_nums[n-1] * c[uniq_nums[n-1]] + dfs(prev_valid_ + 1)

            not_use = dfs(n-1)
            res = max(use_cur, not_use)
            cache[n] = res
            return res
        return dfs(len(uniq_nums))

