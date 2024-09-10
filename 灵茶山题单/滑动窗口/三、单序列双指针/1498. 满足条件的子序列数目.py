MOD = 10 ** 9 + 7


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        j = 0
        res = 0
        for i in range(n - 1, -1, -1):
            # if x * 2 <= target:
            #     print("x * 2, ", x)
            #     res += 1
            x = nums[i]
            if x * 2 > target:
                j = i
                continue
            while j < n and nums[j] + x <= target:
                j += 1
            slen = j - i
            res += 2 ** (j - i - 1)

        return res % MOD

