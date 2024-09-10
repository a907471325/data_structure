class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        arr = [0, 0]

        res = 0
        j = 0
        for i, x in enumerate(s):
            arr[int(x)] += 1
            while arr[0] > k and arr[1] > k:
                arr[int(s[j])] -= 1
                j += 1
            res += i - j + 1
        return res
