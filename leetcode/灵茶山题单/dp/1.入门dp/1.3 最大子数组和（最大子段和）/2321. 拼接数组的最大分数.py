class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        # 差值数组 nums = nums1 - nums2
        # nums的最小和子数组即为nums1 可以从nums2中获得的最大分数，反之亦然
        n = len(nums1)
        f1, f2 = [0] * n, [0] * n
        f1[0] = nums1[0] - nums2[0]
        f2[0] = nums2[0] - nums1[0]

        for i in range(1, n):
            diff1 = nums1[i] - nums2[i]
            diff2 = -diff1
            f1[i] = min(f1[i - 1] + diff1, diff1)
            f2[i] = min(f2[i - 1] + diff2, diff2)

        return max(sum(nums1) - min(f1), sum(nums2) - min(f2))

