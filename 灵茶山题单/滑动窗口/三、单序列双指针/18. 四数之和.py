class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        # print(nums)
        res = []
        n = len(nums)

        for j in range(n - 3):

            if j and nums[j] == nums[j - 1]:
                continue

            if sum(nums[j:j + 4]) > target:
                break

            if sum([nums[j], nums[-3], nums[-2], nums[-1]]) < target:
                continue

            for i in range(j + 1, n - 2):
                l = i + 1
                r = n - 1

                if i > j + 1 and nums[i] == nums[i - 1]:
                    continue

                if sum([nums[j], nums[i], nums[i + 1], nums[i + 2]]) > target:
                    break

                if sum([nums[j], nums[i], nums[-2], nums[-1]]) < target:
                    continue

                while l < r:
                    # print("l:", l, ",r:", r)
                    sum1 = nums[j] + nums[i] + nums[l] + nums[r]
                    if sum1 > target:
                        r -= 1
                    elif sum1 < target:
                        l += 1
                    else:
                        res.append([nums[j], nums[i], nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        r -= 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
        return res
