class Solution:
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:

        dbig = Counter()
        dsmall = Counter(small)

        j = 0
        start = -1
        min_len = 1e9

        target = len(small)
        for i, x in enumerate(big):
            dbig[x] += 1
            if dbig[x] == dsmall[x]:
                target -= 1

            while target == 0:
                if i - j + 1 < min_len:
                    min_len = i - j + 1
                    start = j

                if dbig[big[j]] == dsmall[big[j]]:
                    target += 1
                dbig[big[j]] -= 1
                j += 1

        if start == -1:
            return []

        return [start, start + min_len - 1]




