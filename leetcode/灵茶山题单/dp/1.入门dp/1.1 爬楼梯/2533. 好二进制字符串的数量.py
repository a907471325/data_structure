MOD = 10 ** 9 + 7


class Solution:
    # dfs
    # def goodBinaryStrings(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
    #     # f(n) = f( n - k * a )  0 <= k <= n / a
    #     #        f( n - m * b )  0 <= m <= n / b
    #     ans = 0
    #     cache = [-1] * (maxLength + 1)
    #     for i in range(minLength, maxLength+1):
    #         ans += self.dfs(i, oneGroup, zeroGroup, cache)
    #         ans %= MOD
    #     return ans

    # def dfs(self, n, a, b, cache):
    #     if n < 0:
    #         return 0
    #     if n == 0:
    #         return 1
    #     if cache[n] != -1:
    #         return cache[n]

    #     res = 0
    #     res += self.dfs(n - a, a, b, cache)
    #     res %= MOD
    #     res += self.dfs(n - b, a, b, cache)
    #     res %= MOD
    #     cache[n] = res
    #     return res

    # dp
    def goodBinaryStrings(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
        # f(n) = f( n - a )  + f( n - b )
        f = [0] * (maxLength + 1)
        f[0] = 1
        for i in range(min(oneGroup, zeroGroup), maxLength + 1):
            if i >= oneGroup:
                f[i] += f[i - oneGroup]
            if i >= zeroGroup:
                f[i] += f[i - zeroGroup]
            f[i] %= MOD
        return sum(f[minLength:maxLength + 1]) % MOD
