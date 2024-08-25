class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        targets = set(['a', 'e', 'i', 'o', 'u'])

        cur = 0
        res = 0

        for i in range(len(s)):
            if s[i] in targets:
                cur += 1
            if i < k - 1:
                continue
            res = max(cur, res)
            if s[i - k + 1] in targets:
                cur -= 1

        return res
