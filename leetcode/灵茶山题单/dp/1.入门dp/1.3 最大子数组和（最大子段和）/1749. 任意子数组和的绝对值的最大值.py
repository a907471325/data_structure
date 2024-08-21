from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # -10 13
        # -10 3
        # -10 -3
        # -10 -13
        # 10 13
        # 10 3
        # 10 -13
        # 10 -3
        # 同号 直接相加，异号比大小

        f1 = [0] * (len(nums))
        f2 = [0] * (len(nums))
        f1[0] = nums[0]
        f2[0] = nums[0]
        res = 0
        for i in range(1, len(nums)):
            f1[i] = max(f1[i - 1] + nums[i], nums[i])
            f2[i] = min(f2[i - 1] + nums[i], nums[i])

        return max(max(f1), abs(min(f2)))
