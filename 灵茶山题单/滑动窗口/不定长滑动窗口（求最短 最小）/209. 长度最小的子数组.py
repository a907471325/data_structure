class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        res = 1e9
        j = 0
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]

            while cur_sum >= target:
                res = min(res, i - j + 1)

                cur_sum -= nums[j]
                j += 1

            # if cur_sum >= target:
            #     res = min(res, i-j+1)
        if res == 1e9:
            return 0
        return res
