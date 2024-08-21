from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # 解法1
        # 最大和数组可能为：
        # 1. 在数组内，求最大数组和res1
        # 2. 在环上 nums[j:n] suffix + nums[0:j-1] prefix ,1 <= j <= n 的最大值 res2
        # res = max(res1, res2)
        n = len(nums)
        prefix_sum, suffix_sum = [0] * n, [0] * n
        prefix_sum[0] = nums[0]
        suffix_sum[n - 1] = nums[n - 1]

        min_prefix = min(0, nums[0])
        max_prefix = nums[0]
        res1 = nums[0]
        res2 = -3 * 10 ** 4

        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + nums[i]

        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

            res1 = max(res1, prefix_sum[i] - min_prefix)
            min_prefix = min(prefix_sum[i], min_prefix)

            res2 = max(max_prefix + suffix_sum[i], res2)
            max_prefix = max(max_prefix, prefix_sum[i])

        return max(res1, res2)

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # 解法2
        # 最大和数组可能为：
        # 1. 在数组内，求最大数组和res1
        # 2. 在数组内，求最小数组和sum2, res2 = sum(nums2) - sum2 即为环上最大数组
        # res = max(res1, res2)

        n = len(nums)
        fm, fn = [0] * n, [0] * n
        fm[0] = nums[0]
        fm[0] = nums[0]

        res1 = nums[0]
        res2 = nums[0]

        for i in range(1, n):
            fm[i] = max(fm[i - 1] + nums[i], nums[i])
            res1 = max(res1, fm[i])

            fn[i] = min(fn[i - 1] + nums[i], nums[i])
            res2 = min(res2, fn[i])

        if sum(nums) - res2 == 0:
            return res1
        return max(res1, sum(nums) - res2)









