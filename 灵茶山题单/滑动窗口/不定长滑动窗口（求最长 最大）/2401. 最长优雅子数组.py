class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 1
        i = 1
        j = 0
        cur_sum = nums[j]
        while i < n:
            if nums[i] & cur_sum == 0:
                res = max(res, i - j + 1)
            else:
                while j < i and nums[i] & cur_sum != 0:
                    cur_sum -= nums[j]
                    j += 1
            cur_sum += nums[i]

            i += 1
        return res

