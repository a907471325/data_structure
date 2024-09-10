class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # -4 -1 1 2, target = 1
        # -10 ..... -1
        # 1 ....... 10
        nums = sorted(nums)
        n = len(nums)
        res = 1e9

        for i in range(n - 2):
            l = i + 1
            r = n - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            sum1 = nums[i] + nums[i + 1] + nums[i + 2]
            if sum1 >= target:
                if abs(sum1 - target) < abs(res - target):
                    res = sum1
                    break

            sum2 = nums[i] + nums[r - 1] + nums[r]
            if sum2 < target:
                if abs(sum2 - target) < abs(res - target):
                    res = sum2
                    continue

            while l < r:
                sum3 = nums[l] + nums[r] + nums[i]

                if abs(sum3 - target) < abs(res - target):
                    res = sum3

                if sum3 < target:
                    l += 1
                elif sum3 > target:
                    r -= 1
                else:
                    return target
        return res
