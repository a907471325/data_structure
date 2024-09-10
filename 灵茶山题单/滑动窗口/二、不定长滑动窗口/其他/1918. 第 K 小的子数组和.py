class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        # 1 1 1 2 10
        # 1 , 1 , 1, 2, 10
        # 2 , 2, 3, 12
        # 3, 4, 13
        # 5, 14
        # 15

        n = len(nums)
        l, r = min(nums), sum(nums) + 1
        ans = 0
        while l < r:
            m = l + ((r - l) >> 1)

            cur_sum = 0
            cnt = 0
            j = 0

            for i, x in enumerate(nums):
                cur_sum += x
                while cur_sum > m:
                    cur_sum -= nums[j]
                    j += 1
                cnt += i - j + 1

            if cnt >= k:
                r = m
            else:
                l = m + 1

        return l


