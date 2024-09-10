class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        p = s1
        td = Counter(p)
        match_target = len(td)

        d = {}
        match_num = 0

        for i, x in enumerate(s2):
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
                return True

            l = s2[i - len(p) + 1]
            d[l] -= 1
            if d[l] == td[l]:
                match_num += 1
            elif d[l] + 1 == td[l]:
                match_num -= 1

        return False

