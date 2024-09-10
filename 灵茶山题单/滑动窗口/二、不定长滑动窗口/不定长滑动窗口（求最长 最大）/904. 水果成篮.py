class Solution:
    def totalFruit(self, nums: List[int]) -> int:

        d = {}

        res = 0
        j = 0
        uniq_num = 0

        for i,x in enumerate(nums):
            if x not in d:
                d[x] = 0

            d[x] += 1
            if d[x] == 1:
                uniq_num += 1

            while uniq_num > 2:
                d[nums[j]] -= 1
                if d[nums[j]] == 0:
                    uniq_num -= 1
                j += 1
            res = max(res, i-j+1)
        return res
