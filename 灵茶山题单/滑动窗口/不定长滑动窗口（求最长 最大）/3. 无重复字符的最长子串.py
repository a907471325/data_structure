class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        d = {}
        d[s[0]] = 1
        j = 0
        res = 1
        for i in range(1, len(s)):
            if s[i] not in d:
                d[s[i]] = 0
            d[s[i]] += 1
            while d[s[i]] > 1:
                d[s[j]] -= 1
                j += 1
            res = max(res, i-j+1)
        return res
