MOD = 10 ** 9 + 7
class Solution:
    def countHousePlacements(self, n: int) -> int:
        # 全部分布 = 全为空 + 第一条街排列数量 + 第二条街排列数量 + 第一条街排列数量 * 第二条街排列数量
        # all = 1 + num1 + num1 + num1 * num1 = (num1 + 1) ^ 2
        # 长为i街道的排列数量 f[i] = f[i-2] + f[i-1]


        f = [0] * (n + 1)
        f[0] = 1
        f[1] = 2

        for i in range(2, n+1):
            f[i] = (f[i-2] + f[i-1]) % MOD
        return (f[n] * f[n]) % MOD
