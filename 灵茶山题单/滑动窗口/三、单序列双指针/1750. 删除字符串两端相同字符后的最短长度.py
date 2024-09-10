class Solution:
    def minimumLength(self, s: str) -> int:

        n = len(s)

        i = 0
        j = n - 1
        while i < j and s[i] == s[j]:
            cur = s[i]
            while i <= j and s[i] == cur:
                i += 1
            while i <= j and s[j] == cur:
                j -= 1

        return j - i + 1





