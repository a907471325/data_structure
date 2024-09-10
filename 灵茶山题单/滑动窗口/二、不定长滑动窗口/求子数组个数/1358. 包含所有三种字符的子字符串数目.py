class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # a b c a b c
        # a b c
        # a b c a , b c a
        # a b c a b, b c a b, c a b
        # a b c a b c, b c a b c, c a b c, a b c



        d = {'a':0, "b":0, "c": 0}

        n = len(s)
        j = -1
        res = 0

        for i, x in enumerate(s):
            while j < n and (d['a'] < 1 or d['b'] < 1 or d['c'] < 1):
                j += 1
                if j == n:
                    break
                d[s[j]] += 1
            d[x] -= 1
            # print(j)
            res += n - j

        return res

