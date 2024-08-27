class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # nums =  1 4 8 13 , k = 5
        nums = sorted(nums)
        used = 0
        j = 0
        res = 1

        for i in range(1, len(nums)):
            # print(nums[i])
            cost = (nums[i] - nums[i-1]) * (i - j)
            used += cost
            while j < i and used > k:
                used -= (nums[i] - nums[j])
                j += 1
            # print(j,",",i)
            # print(used)
            if used > 0 or (used == 0 and nums[i] == nums[j]):
                res = max(res, i-j+1)
        return res
