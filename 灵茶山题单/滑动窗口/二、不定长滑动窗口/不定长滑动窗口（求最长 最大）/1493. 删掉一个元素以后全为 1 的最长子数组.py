class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        znum = 0
        if nums[0] == 0:
            znum = 1

        res = 1
        j = 0
        for i in range(1, len(nums)):
            if nums[i] == 0:
                znum += 1
            while znum > 1:
                if nums[j] == 0:
                    znum -= 1
                j += 1

            res = max(i-j+1, res)

        return res - 1

