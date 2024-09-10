import string

class Solution:
    def countCompleteSubstrings(self, word: str, count: int) -> int:
        # 预处理 每个位置与前一个位置差值不超过2..
        res = 0
        s = word
        n = len(s)
        valid_words = []
        i = 0
        while i < n:
            start = i
            i += 1
            while i < n and abs(ord(s[i]) - ord(s[i - 1])) <= 2:
                i += 1
            valid_words.append(s[start:i])

        for s in valid_words:
            for k in [count * j for j in range(1, 27)]:
                if k > len(s):
                    break

                d = {ch:0 for ch in string.ascii_lowercase}
                uniq_num = 0

                for i, x in enumerate(s):

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