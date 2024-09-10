class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        j = 0
        res = 0
        sumji = 0
        for i, x in enumerate(nums):
            sumji += x
            while sumji * (i - j + 1) >= k:
                sumji -= nums[j]
                j += 1

            if sumji != 0:
                res += i - j + 1
        return res


