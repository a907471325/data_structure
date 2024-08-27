class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:


        res = 0
        for i in range(1, k+1):
            ch_num = 0
            j = 0

            d = {}
            for i, x in enumerate(s):
                if x not in d:
                    d[x] = 0
                d[x] += 1
                if d[x] == 1:
                    ch_num += 1

                while ch_num > k:
                    d[s[j]] -= 1
                    if d[s[j]] == 0:
                        ch_num -= 1
                    j += 1

                res = max(res, i - j + 1)
        return res
