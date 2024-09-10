class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        nums = sorted(tokens)
        n = len(nums)
        res = 0
        p = 0
        l = 0
        r = n-1
        while l <= r:
            if power >= nums[l]:
                power -= nums[l]
                p += 1
                res = max(p, res)
                l += 1
            elif p > 0:
                power += nums[r]
                p -= 1
                r -= 1
            else:
                return 0
        return res
