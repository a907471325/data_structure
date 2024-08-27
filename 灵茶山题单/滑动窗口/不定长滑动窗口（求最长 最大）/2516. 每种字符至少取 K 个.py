class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # 逆向思维，取每种字符至多取 cnt(ch) - k个的最长子串\
        if k == 0:
            return 0

        ds = Counter(s)
        dt = Counter()
        dt['a'] = ds['a'] - k
        dt['b'] = ds['b'] - k
        dt['c'] = ds['c'] - k

        # if ds['a'] == 0 or ds['b'] == 0 or ds['c'] == 0:
        #     return -1
        if ds['a'] < k or ds['b'] < k or ds['c'] < k:
            return -1

        if dt['a'] == dt['b'] == dt['c'] == 0:
            return len(s)

        max_len = 0
        d = Counter()

        j = 0
        for i, x in enumerate(s):
            d[x] += 1
            while j <= i and d[x] > dt[x]:
                d[s[j]] -= 1
                j += 1
            max_len = max(max_len, i - j + 1)

        if max_len == 0:
            return -1

        return len(s) - max_len

