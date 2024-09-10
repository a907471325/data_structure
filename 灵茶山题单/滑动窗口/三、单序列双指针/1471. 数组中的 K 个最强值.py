class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        arr = sorted(arr)
        m = arr[(n - 1) // 2]

        i = 0
        j = n - 1
        res = []
        num = 0
        while i < j and num < k:
            val = abs(arr[i] - m) > abs(arr[j] - m)
            if val > 0:
                res.append(arr[i])
                i += 1
            elif val < 0:
                res.append(arr[j])
                j -= 1
            elif arr[i] > arr[j]:
                res.append(arr[i])
                i += 1
            else:
                res.append(arr[j])
                j -= 1
            num += 1
        if num != k:
            res.append(arr[i])
        return res

