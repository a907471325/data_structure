class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:

        d = {}

        uniq_num = 0
        res = []
        for i, x in enumerate(nums):
            if x not in d:
                d[x] = 0

            if d[x] == 0:
                uniq_num += 1
            d[x] += 1

            if i < k - 1:
                continue

            res.append(uniq_num)
            if d[nums[i - k + 1]] == 1:
                uniq_num -= 1
            d[nums[i - k + 1]] -= 1

        return res