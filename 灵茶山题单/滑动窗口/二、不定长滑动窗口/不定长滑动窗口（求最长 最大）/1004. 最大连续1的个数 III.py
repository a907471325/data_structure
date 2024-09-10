class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        other_num = 0
        j = 0
        res = 0
        for i, x in enumerate(nums):
            if x == 0:
                other_num += 1
            while other_num > k:
                if nums[j] == 0:
                    other_num -= 1
                j += 1
            res = max(res, i - j + 1)
        return res