class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # cardPoints = [1,2,3,4,5,6,1], k = 3
        # 可行的策略
        # 左边取0个，右边取三个
        # 左边取一个，右边取两个
        # 左边取两个，右边取一个
        # 左边取三个，右边取0个
        # 相当于找长度为 len(cardPoints) - k 的子数组的最小值 t
        #  sum(cardPoints) - t 即为结果

        n = len(cardPoints)
        kk = n - k

        if kk == 0:
            return sum(cardPoints)

        res = 1e9
        cur = 0
        for i, x in enumerate(cardPoints):
            cur += x
            if i < kk - 1:
                continue
            res = min(res, cur)

            cur -= cardPoints[i - kk + 1]

        return sum(cardPoints) - res


