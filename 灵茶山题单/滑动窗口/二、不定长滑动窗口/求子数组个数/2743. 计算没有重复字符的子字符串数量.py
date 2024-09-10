class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:

        d = Counter()
        res = j = 0

        for i, x in enumerate(s):
            d[x] += 1
            while d[x] > 1:
                d[s[j]] -= 1
                j += 1
            res += i - j + 1
        return res