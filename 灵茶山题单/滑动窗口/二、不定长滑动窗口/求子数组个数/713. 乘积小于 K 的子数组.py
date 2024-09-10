class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # [10, 5, 2, 6]
        # 10 , 10 + 10  5 + 5,
        if k == 0:
            return 0

        j = 0
        res = 0
        prod = 1
        for i, x in enumerate(nums):
            prod *= x
            while j < i and prod >= k:
                prod = prod // nums[j]
                j += 1

            if prod < k:
                res += i - j + 1
        return res


