class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        l = 0
        r = len(nums) - 1
        res = -1
        while l < r:
            sum1 = nums[l] + nums[r]
            if sum1 < k:
                res = max(res, sum1)
                l += 1
            elif sum1 >= k:
                r -= 1
        return res
