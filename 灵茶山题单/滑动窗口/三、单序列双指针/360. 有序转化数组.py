class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:

        n = len(nums)
        l = 0
        r = n - 1
        res = []
        while l <= r:
            lsum = nums[l] ** 2 * a + b * nums[l] + c
            bsum = nums[r] ** 2 * a + b * nums[r] + c
            if a >= 0:
                if lsum >= bsum:
                    res.insert(0, lsum)
                    l += 1
                else:
                    res.insert(0, bsum)
                    r -= 1
            else:
                if lsum >= bsum:
                    res.append(bsum)
                    r -= 1
                else:
                    res.append(lsum)
                    l += 1

        return res