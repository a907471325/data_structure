class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        res = 0

        for i in range(n - 1, 1, -1):
            l = 0
            r = i - 1

            while l < r:
                if nums[l] + nums[r] <= nums[i]:
                    l += 1
                else:
                    res += r - l
                    r -= 1
        return res




