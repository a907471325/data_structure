class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        lmax = height[0]
        rmax = height[n-1]

        l = 1
        r = n - 2
        res = 0
        while l <= r:
            if lmax <= rmax:
                area = max(0, lmax - height[l])
                res += area
                lmax = max(lmax, height[l])
                l += 1
            else:
                area = max(0, rmax - height[r])
                res += area
                rmax = max(rmax, height[r])
                r -= 1
        return res
