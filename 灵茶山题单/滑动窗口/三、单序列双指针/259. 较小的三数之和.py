class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        # -2 0 1 3
        n = len(nums)
        nums = sorted(nums)
        if n < 3:
            return 0

        res = 0
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            if sum(nums[i:i + 3]) >= target:
                break
            if nums[i] + nums[-2] + nums[-1] < target:
                res += (r - l + 1) * (r - l) // 2
                continue

            while l < r:
                sum1 = nums[i] + nums[l] + nums[r]
                if sum1 >= target:
                    r -= 1
                else:
                    res += r - l
                    l += 1
        return res