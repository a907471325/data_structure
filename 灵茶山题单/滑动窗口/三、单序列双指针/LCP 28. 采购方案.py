MOD = 10 ** 9 + 7
class Solution:
    def purchasePlans(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        i=0
        j=len(nums) - 1
        res = 0
        while i<j:
            if nums[i] + nums[j] <= target:
                res += j-i
                i += 1
            else:
                j -= 1
        return res % MOD