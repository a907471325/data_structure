class Solution:
    # # n ^ 3
    # def longestNiceSubstring(self, s: str) -> str:

    #     n = len(s)
    #     res = ""
    #     for i in range(n-1):
    #         for j in range(i+1, n):
    #             d = {}
    #             for ch in s[i:j+1]:
    #                 if ch not in d:
    #                     d[ch] = 0
    #                 d[ch] += 1
    #             valid = True
    #             for ch in d.keys():
    #                 if ord(ch) >= ord("A") and ord(ch) <= ord("Z"):
    #                     if chr(ord(ch) + 32) not in d:
    #                         valid = False
    #                 if ord(ch) >= ord("a") and ord(ch) <= ord("z"):
    #                     if chr(ord(ch) - 32) not in d:
    #                         valid = False
    #             if valid and (j-i+1) > len(res):
    #                 res = s[i:j+1]
    #     return res

    # 26 * n * n
    def longestNiceSubstring(self, s: str) -> str:

        res = ""
        for k in range(2, 2 * 26 + 1, 2):

            j = 0
            d = {}
            num = 0
            for i, x in enumerate(s):
                if x not in d:
                    d[x] = 0
                d[x] += 1

                if d[x] == 1:
                    num += 1

                while num > k:
                    d[s[j]] -= 1
                    if d[s[j]] == 0:
                        num -= 1
                    j += 1

                valid = True
                if num == k:
                    for ch in d.keys():
                        if d[ch] == 0:
                            continue
                        if ord("A") <= ord(ch) <= ord("Z"):
                            if chr(ord(ch) + 32) not in d or d[chr(ord(ch) + 32)] == 0:
                                valid = False
                        if ord("a") <= ord(ch) <= ord("z"):
                            if chr(ord(ch) - 32) not in d or d[chr(ord(ch) - 32)] == 0:
                                valid = False
                    if valid and (i - j + 1) > len(res):
                        res = s[j:i + 1]
        return res




