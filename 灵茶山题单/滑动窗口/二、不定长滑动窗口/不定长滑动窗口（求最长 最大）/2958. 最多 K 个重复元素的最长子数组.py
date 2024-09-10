class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        d = {}
        res = 0
        j = 0

        for i,x in enumerate(nums):
            if x not in d:
                d[x] = 0

            d[x] += 1
            while d[x] > k:
                d[nums[j]] -= 1
                j += 1
            res = max(res, i-j+1)
        return res
