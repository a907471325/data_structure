class Solution:
    def maxRepOpt1(self, text: str) -> int:

        dstr = Counter(text)

        res = 1
        j = 0
        d = Counter()

        for i, x in enumerate(text):
            d[x] += 1
            while i - j + 1 - max(d.values()) > 1:
                d[text[j]] -= 1
                if d[text[j]] == 0:
                    del d[text[j]]
                j += 1
            if len(d) == 1:
                res = max(res, i - j + 1)
            for k, v in d.items():
                if v == max(d.values()) and dstr[k] - v > 0:
                    res = max(res, i - j + 1)
        return res


