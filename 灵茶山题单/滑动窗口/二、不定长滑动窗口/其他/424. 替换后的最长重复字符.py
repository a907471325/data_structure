class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if k == n - 1 or k == n:
            return n

        def count_max_freq(arr):
            res = 0
            for num in arr:
                res = max(res, num)
            return res

        j = 0
        res = 0
        max_freq = 0
        count = [0] * 26

        for i in range(n):
            right_key = ord(s[i]) - ord("A")
            count[right_key] += 1

            if max_freq < count[right_key]:
                max_freq = count[right_key]

            if i - j + 1 - max_freq > k:
                left_key = ord(s[j]) - ord("A")
                count[left_key] -= 1
                # max_freq = count_max_freq(count)
                j += 1
            res = max(res, i - j + 1)

        return res






