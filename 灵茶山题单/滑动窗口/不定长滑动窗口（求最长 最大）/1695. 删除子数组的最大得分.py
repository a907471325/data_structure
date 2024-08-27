class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        d = {}
        res = 0
        j = 0
        cur_sum = 0
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 0
            d[nums[i]] += 1
            cur_sum += nums[i]
            while d[nums[i]] > 1:
                d[nums[j]] -= 1
                cur_sum -= nums[j]
                j += 1
            res = max(cur_sum, res)
        return res
