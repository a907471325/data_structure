class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # 1 2 3 4 5 6 7 4 5

        # 先找后缀最大升序数组
        # max (最大前缀升序数组 ,  前缀升序数组 + 后缀最大升序数组)
        n = len(arr)
        j = n - 1
        ans = 0

        while j > 0 and arr[j] >= arr[j - 1]:
            ans = max(ans, n - j + 1)
            j -= 1

        if j == 0:
            return 0

        pre = -1
        for i, x in enumerate(arr):
            if x < pre:
                break
            pre = x
            while j < n and x > arr[j]:
                j += 1
            ans = max(ans, i + 1 + n - j)
        return n - ans





