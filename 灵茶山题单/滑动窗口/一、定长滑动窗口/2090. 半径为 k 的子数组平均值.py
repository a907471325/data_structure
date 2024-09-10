class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # l m r
        # r = i , m = (l + r) >> 1
        if k == 0:
            return nums
        res = [-1] * len(nums)

        cur = 0
        line = 2 * k + 1
        for i, x in enumerate(nums):
            cur += x
            if i < line - 1:
                continue
            m = (2 * i - line + 1) // 2
            res[m] = int(cur // line)
            cur -= nums[i - line + 1]
        return res
