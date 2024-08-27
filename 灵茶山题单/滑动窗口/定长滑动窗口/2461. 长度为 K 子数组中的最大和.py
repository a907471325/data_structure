class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        d = {}
        res = 0
        uniq_num = 0
        cur_sum = 0

        for i, v in enumerate(nums):
            if v not in d:
                d[v] = 0
            d[v] += 1
            if d[v] == 1:
                uniq_num += 1
            elif d[v] == 2:
                uniq_num -= 1

            cur_sum += v
            if i < k - 1:
                continue
            if uniq_num == k:
                res = max(res, cur_sum)

            left = nums[i - k + 1]
            cur_sum -= left

            d[left] -= 1
            if d[left] == 1:
                uniq_num += 1
            elif d[left] == 0:
                uniq_num -= 1

        return res


