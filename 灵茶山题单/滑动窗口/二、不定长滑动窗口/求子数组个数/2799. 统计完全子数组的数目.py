class Solution:
    # 遍历left
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        t = len(set(nums))
        j = -1
        d = Counter()
        res = 0
        for i, x in enumerate(nums):
            while j < len(nums) and t > 0:
                j += 1
                if j == n:
                    break
                d[nums[j]] += 1
                if d[nums[j]] == 1:
                    t -= 1
            if t == 0:
                res += len(nums) - j
            d[x] -= 1
            if d[x] == 0:
                t += 1
        return res

