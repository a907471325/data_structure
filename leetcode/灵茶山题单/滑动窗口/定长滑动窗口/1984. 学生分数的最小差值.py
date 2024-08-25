class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        res = 1e9
        for i in range(len(nums)):
            if i < k - 1:
                continue
            res = min(res, nums[i] - nums[i-k+1])
        return res



