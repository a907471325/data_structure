class Solution:
    # o 52 * n + m
    # def minWindow(self, s: str, t: str) -> str:
    #     ds = {}
    #     dt = {}

    #     for ss in s:
    #         ds[ss] = 0

    #     for tt in t:
    #         if tt not in dt:
    #             dt[tt] = 0
    #         dt[tt] += 1

    #     res_len = 1e9
    #     res_start = -1

    #     def check(ds, dt):
    #         valid = True
    #         for k,v in dt.items():
    #             if k not in ds or ds[k] < v:
    #                 valid = False
    #                 break
    #         return valid

    #     j = 0
    #     for i, x in enumerate(s):
    #         ds[x] += 1

    #         while check(ds, dt):

    #             if i - j + 1 < res_len:
    #                 res_len = i - j + 1
    #                 res_start = j

    #             ds[s[j]] -= 1
    #             j += 1

    #     if res_start == -1:
    #         return ""

    #     return s[res_start:res_start+res_len]

    # n
    def minWindow(self, s: str, t: str) -> str:
        ds = {}
        dt = {}

        for ss in s:
            ds[ss] = 0

        for tt in t:
            if tt not in dt:
                dt[tt] = 0
            dt[tt] += 1

        res_len = 1e9
        res_start = -1
        j = 0
        target = len(dt)

        for i, x in enumerate(s):
            ds[x] += 1
            if x in dt and ds[x] == dt[x]:
                target -= 1

            while target == 0:

                if i - j + 1 < res_len:
                    res_len = i - j + 1
                    res_start = j
                if s[j] in dt and ds[s[j]] == dt[s[j]]:
                    target += 1
                ds[s[j]] -= 1
                j += 1

        if res_start == -1:
            return ""

        return s[res_start:res_start + res_len]




