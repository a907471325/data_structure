class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # 最终方案数f[l ~ h] = f[h] - f[l-1]
        # f[i] = f[i - one * '1'] + f[i - zero * '0']

        MOD = 1_000_000_007
        MOD = int(1e9 + 7)
        # MOD = 10 ** 9 + 7
        def mod(a):
            return a % MOD

        cache = [-1] * (high + 1)
        def dfs(target):
            if target < 0:
                return 0
            if target == 0:
                return 1
            if cache[target] != -1:
                return cache[target]
            res = dfs(target - zero) + dfs(target - one)
            res = mod(res)
            cache[target] = res
            return res

        ans = 0
        while high >= low:
            ans += dfs(high)
            ans = mod(ans)
            high -= 1
        return ans

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # 最终方案数f[l ~ h] = f[h] - f[l-1]
        # f[i] = f[i - one * '1'] + f[i - zero * '0']

        MOD = 1_000_000_007
        MOD = int(1e9 + 7)
        # MOD = 10 ** 9 + 7

        f = [0] * (high + 1)
        f[0] = 1
        for i in range(high + 1):
            if i >= zero:
                f[i] += f[i - zero]
                f[i] = f[i] % MOD
            if i >= one:
                f[i] += f[i - one]
                f[i] = f[i] % MOD

        ans = 0
        while high >= low:
            ans += f[high]
            ans = ans % MOD
            high -= 1
        return ans


if __name__ == '__main__':
    so = Solution()
    params = [200, 200, 10, 1]
    result = so.countGoodStrings(params[0], params[1], params[2], params[3])
    print(result)
