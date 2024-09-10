class Solution:
    # left遍历
    # def countSubarrays(self, nums: List[int], k: int) -> int:
    #     max_elem = max(nums)
    #     cnt = 0
    #     j = -1
    #     res = 0
    #     n = len(nums)
    #     for i, x in enumerate(nums):
    #         while j < n and cnt < k:
    #             j += 1
    #             if j == n:
    #                 break
    #             if nums[j] == max_elem:
    #                 cnt += 1
    #         if cnt == k:
    #             res += len(nums) - j
    #         if x == max_elem:
    #             cnt -= 1
    #     return res

    # right遍历
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_elem = max(nums)
        cnt = 0
        j = 0
        res = 0
        n = len(nums)
        for i, x in enumerate(nums):
            if x == max_elem:
                cnt += 1
            while cnt == k:
                if nums[j] == max_elem:
                    cnt -= 1
                j += 1
            res += j
        return res

