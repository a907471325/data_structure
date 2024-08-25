class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        res = -1e9
        cur = 0

        for i, x in enumerate(nums):
            cur += x
            if i < k - 1:
                continue
            res = max(res, cur)
            cur -= nums[i-k+1]
        return res / k
