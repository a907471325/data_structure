class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        d = {i: 0 for i in range(-50, 51)}

        def get_b_value():
            total = 0
            for v in range(-50, 0):
                if d[v]:
                    total += d[v]
                if total >= x:
                    if v < 0:
                        return v
                    else:
                        break
            return 0

        res = []
        for i, t in enumerate(nums):
            d[t] += 1
            if i < k - 1:
                continue
            res.append(get_b_value())
            d[nums[i - k + 1]] -= 1

        return res