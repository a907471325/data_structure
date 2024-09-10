class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        l = 0
        r = n - 1

        ln = 0
        rn = 0

        while l < r:
            if nums[l] + ln < nums[r] + rn:
                ln += nums[l]
                l += 1
                res += 1
            elif nums[l] + ln > nums[r] + rn:
                rn += nums[r]
                r -= 1
                res += 1
            else:
                ln = rn = 0
                l += 1
                r -= 1
        return res


