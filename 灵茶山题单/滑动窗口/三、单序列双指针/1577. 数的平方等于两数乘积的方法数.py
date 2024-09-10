class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        return self.helper(nums1, nums2) + self.helper(nums2, nums1)

    def helper(self, nums1, nums2):
        # 1 1 1  1 1 1/ 15

        # 1 1 4 4 12

        res = 0
        m = len(nums1)
        n = len(nums2)
        if n < 2:
            return res
        for i in range(m):
            l = 0
            r = n - 1

            t = nums1[i] ** 2
            if nums2[0] * nums2[1] > t:
                continue

            if nums2[-1] * nums2[-2] < t:
                break

            while l < r:
                p = nums2[l] * nums2[r]
                if p > t:
                    r -= 1
                elif p < t:
                    l += 1
                else:
                    is_eq = nums2[l] == nums2[r]
                    if is_eq:
                        slen = r - l + 1
                        res += (slen - 1) * (slen) // 2
                        break

                    j = l + 1
                    k = r - 1
                    while nums2[j] == nums2[l]:
                        j += 1

                    while nums2[k] == nums2[r]:
                        k -= 1

                    res += (j - l) * (r - k)
                    l = j
                    r = k

        return res
