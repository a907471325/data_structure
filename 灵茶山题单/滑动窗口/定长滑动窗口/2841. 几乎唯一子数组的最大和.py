class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        # hashmap记录窗口内数字频次 d = {num: t}
        # uniq_num = k
        # 进入时如果不在dict或者t==0, uniq_num += 1
        # 退出时如果t==1, uniq_num -= 1
        d = {}

        uniq_num = 0
        res = cur_sum = 0
        for i, x in enumerate(nums):
            if x not in d:
                d[x] = 0

            if d[x] == 0:
                uniq_num += 1
            d[x] += 1

            cur_sum += x

            if i < k - 1:
                continue

            if uniq_num >= m:
                res = max(res, cur_sum)

            if d[nums[i - k + 1]] == 1:
                uniq_num -= 1
            d[nums[i - k + 1]] -= 1
            cur_sum -= nums[i - k + 1]

        return res

