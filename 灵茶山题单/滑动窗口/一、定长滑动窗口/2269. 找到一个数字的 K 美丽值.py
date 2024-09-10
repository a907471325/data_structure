class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:

        num_s = str(num)
        cur = ''
        res = 0
        for i in range(len(num_s)):
            cur = cur + num_s[i]
            if i < k - 1:
                continue
            if int(cur) and num % int(cur) == 0:
                res += 1
            cur = cur[1:]
        return res