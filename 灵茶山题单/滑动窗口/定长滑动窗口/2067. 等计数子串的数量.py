class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:
        # 总共有26个字母，窗口范围 3 * 1 - 3 * 26

        res = 0
        for k in [count * j for j in range(1, 27)]:
            d = {}
            uniq_num = 0
            for i, x in enumerate(s):
                if x not in d:
                    d[x] = 0

                d[x] += 1
                if d[x] == count:
                    uniq_num += 1
                elif d[x] == count+1:
                    uniq_num -= 1

                if i < k - 1:
                    continue

                if uniq_num * count == k:
                    res += 1

                if d[s[i - k + 1]] == count:
                    uniq_num -= 1
                if d[s[i - k + 1]] == count+1:
                     uniq_num += 1
                d[s[i - k + 1]] -= 1

        return res