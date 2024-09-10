# arr_nums = [0, 0, 1]
# for i in range(3, 10**5+1):
#     arr_nums.append(arr_nums[-1] + i - 1)

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # 1 1 1 1 1 = 4. 3 2 1

        pairs = 0
        j = 0
        n = len(nums)
        d = Counter()
        res = 0
        for i, x in enumerate(nums):
            d[x] += 1
            if d[x] >= 2:
                pairs += d[x] - 1
            while pairs >= k:
                if d[nums[j]] >= 2:
                    pairs -= d[nums[j]] - 1
                d[nums[j]] -= 1
                j += 1
            res += j
        return res





