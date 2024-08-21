from typing import List

MOD = 10 ** 9 + 7


class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        # 1,-2,1, 1,-2,1, 1,-2,1, 1,-2,1, 1,-2,1
        total = sum(arr)
        max_sub = self.maxSubArray(arr)
        n = len(arr)
        prefix, suffix = [0] * n, [0] * n
        prefix[0] = arr[0]
        suffix[n - 1] = arr[n - 1]
        for i in range(1, len(arr)):
            prefix[i] = prefix[i - 1] + arr[i]
        for i in reversed(range(0, len(arr) - 1)):
            suffix[i] = suffix[i + 1] + arr[i]
        if k == 1:
            return max(max_sub, 0)
        return max(max_sub, k * total, max(prefix) + max(suffix), max(prefix) + max(suffix) + (k - 2) * total, 0) % MOD

    def maxSubArray(self, nums: List[int]) -> int:
        ans = -1e9
        min_pre_sum = pre_sum = 0
        for x in nums:
            pre_sum += x  # 当前的前缀和
            ans = max(ans, pre_sum - min_pre_sum)  # 减去前缀和的最小值
            min_pre_sum = min(min_pre_sum, pre_sum)  # 维护前缀和的最小值
        return ans

