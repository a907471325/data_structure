class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #
        nums = sorted(nums)
        # print(nums)
        res = []
        target = 0
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1

            if i and nums[i] == nums[i - 1]:
                continue

            if sum(nums[i:i + 3]) > target:
                break

            if sum([nums[i], nums[r - 1], nums[r]]) < target:
                continue

            while l < r:
                # print("l:", l, ",r:", r)
                sum1 = nums[i] + nums[l] + nums[r]
                if sum1 > target:
                    r -= 1
                elif sum1 < target:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res




