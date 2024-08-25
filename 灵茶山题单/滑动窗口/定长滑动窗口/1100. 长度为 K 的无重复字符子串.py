class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:

        d = {}

        uniq_num = 0
        res = 0
        for i, x in enumerate(s):
            if x not in d:
                d[x] = 0

            if d[x] == 0:
                uniq_num += 1
            d[x] += 1

            if i < k - 1:
                continue

            if uniq_num == k:
                res += 1
            if d[s[i - k + 1]] == 1:
                uniq_num -= 1
            d[s[i - k + 1]] -= 1

        return res