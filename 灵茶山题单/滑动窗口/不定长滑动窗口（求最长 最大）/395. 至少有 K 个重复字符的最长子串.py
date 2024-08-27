class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        res = 0
        for w in range(1, 27):
            d = {}
            j = 0
            num = 0
            target_num = 0
            for i, x in enumerate(s):
                if x not in d:
                    d[x] = 0
                d[x] += 1
                if d[x] == 1:
                    num += 1
                if d[x] == k:
                    target_num += 1

                while num > w:
                    d[s[j]] -= 1
                    if d[s[j]] == 0:
                        num -= 1
                    if d[s[j]] == k - 1:
                        target_num -= 1
                    j += 1

                if target_num == w:
                    res = max(i - j + 1, res)
        return res

