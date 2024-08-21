from typing import List


class Solution:

    # dp
    # def maxSubArray(self, nums: List[int]) -> int:
    #     # f[i] = max(f[i-1] + nums[i], nums[i])

    #     n = len(nums)
    #     f = [0] * n
    #     f[0] = nums[0]
    #     for i in range(1, n):
    #         f[i] = max(f[i-1] + nums[i], nums[i])
    #     return max(f)

    def maxSubArray(self, nums: List[int]) -> int:
        ans = -1e9
        min_pre_sum = pre_sum = 0
        for x in nums:
            pre_sum += x  # 当前的前缀和
            ans = max(ans, pre_sum - min_pre_sum)  # 减去前缀和的最小值
            min_pre_sum = min(min_pre_sum, pre_sum)  # 维护前缀和的最小值
        return ans

