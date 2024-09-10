class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # 0 1 2 3, k = 10
        # 2 + 1 , (j-i )* (1+j-i )
        nums = sorted(nums)
        i = 0
        j = len(nums)-1
        res = 0
        while i < j:
            if nums[i] + nums[j] >= target:
                j -= 1
            else:
                res += j-i
                i += 1
        return res