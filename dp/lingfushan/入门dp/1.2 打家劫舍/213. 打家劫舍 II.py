from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        return max(self.rob1(nums[:n-1]), nums[n-1] + self.rob1(nums[1:n-2]))




    def rob1(self, nums: List[int]) -> int:
        # f(n) = max( f(n-1) , f(n-2) + nums[n] )
        if not nums:
            return 0
        n = len(nums)
        f = [0] * (n + 1)
        f[1] = nums[0]
        for i in range(2, len(nums)+1):
            f[i] = max(f[i-1], f[i-2] + nums[i-1])
        return f[len(nums)]