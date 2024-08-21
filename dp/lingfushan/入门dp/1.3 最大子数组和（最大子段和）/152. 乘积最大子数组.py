from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 2 3 4 2 0
        # 2 6 24 48 0
        # 2 3 4 2 0

        # -1 -2 -3 -1 0
        # -1  2  6  6 0
        # -1 -2 -6 -6 0
        n = len(nums)
        fmax, fmin = [0] * n, [0] * n
        fmax[0] = nums[0]
        fmin[0] = nums[0]

        for i in range(1, n):
            fmax[i] = max(nums[i] * fmax[i-1], nums[i] * fmin[i-1], nums[i])
            fmin[i] = min(nums[i] * fmax[i-1], nums[i] * fmin[i-1], nums[i])
        return max(fmax)

