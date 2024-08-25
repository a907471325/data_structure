class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        td = Counter(p)
        match_target = len(td)

        d = {}
        match_num = 0
        res = []

        for i, x in enumerate(s):
            if x not in d:
                d[x] = 0
            d[x] += 1

            if d[x] == td[x]:
                match_num += 1
            elif d[x] == td[x] + 1:
                match_num -= 1

            if i < len(p) - 1:
                continue

            if match_num == match_target:
                res.append(i - len(p) + 1)

            d[s[i - len(p) + 1]] -= 1
            if d[s[i - len(p) + 1]] == td[s[i - len(p) + 1]]:
                match_num += 1
            elif d[s[i - len(p) + 1]] + 1 == td[s[i - len(p) + 1]]:
                match_num -= 1

        return res

