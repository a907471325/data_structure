class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:

        nums = [int(_) for _ in s]

        znum = 0

        res = 1
        j = 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 0:
                znum += 1
            while znum > 1:
                if nums[j] - nums[j+1] == 0:
                    znum -= 1
                j += 1

            res = max(i-j+1, res)

        return res

