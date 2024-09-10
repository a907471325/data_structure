class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        # 与1052题思路类似
        # candies = [1,2,2,3,4,3], k = 3
        # l = 3 = len(candies) - k
        # 可以在左边剩余3个
        # 可以在左边剩余2个，右边1个
        # 可以在左边剩余1个，右边2个
        # 可以在左边剩余0个，右边3个

        n = len(candies)
        l = n - k
        if l == 0:
            return 0

        d = {}
        uniq_num = 0
        res = 0
        for i, x in enumerate(candies[:l]):
            if x not in d:
                d[x] = 0
            d[x] += 1
            if d[x] == 1:
                uniq_num += 1
            res = max(res, uniq_num)

        j = l - 1
        for i in range(1, l + 1):
            t = candies[j]
            d[t] -= 1
            if d[t] == 0:
                uniq_num -= 1
            j -= 1

            x = candies[n - i]
            if x not in d:
                d[x] = 0

            d[x] += 1
            if d[x] == 1:
                uniq_num += 1
            res = max(res, uniq_num)

        return res





