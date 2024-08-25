class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        thres = threshold * k

        res = 0
        cur = 0
        for i, x in enumerate(arr):
            cur += x
            if i < k - 1:
                continue
            if cur >= thres:
                res += 1
            cur -= arr[i-k+1]
        return res