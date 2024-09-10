class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        k = sum(nums) - x
        if k == 0:
            return len(nums)
        j = 0
        res = -1
        cur_sum = 0
        for i,x in enumerate(nums):
            cur_sum += x
            while j < i and cur_sum > k:
                cur_sum -= nums[j]
                j += 1
            if cur_sum == k:
                res = max(i-j+1, res)
        if res == -1:
            return res
        return len(nums) - res

