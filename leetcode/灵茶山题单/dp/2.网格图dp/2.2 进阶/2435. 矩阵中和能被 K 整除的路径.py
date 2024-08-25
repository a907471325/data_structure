class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:

        mod = 10 ** 9 + 7

        l, n = len(grid), len(grid[0])
        f = [[[0] * k for _ in range(n)] for _ in range(l)]

        for m in range(k):
            f[0][0][m] = 1 if grid[0][0] % k == m else 0

        for i in range(1, l):
            num = grid[i][0] % k
            for m in range(k):
                idx = (m + num) % k
                f[i][0][idx] = f[i - 1][0][m]

        for j in range(1, n):
            num = grid[0][j] % k
            for m in range(k):
                idx = (m + num) % k
                f[0][j][idx] = f[0][j - 1][m]

        for i in range(1, l):
            for j in range(1, n):
                num = grid[i][j] % k
                for m in range(k):
                    idx = (m + num) % k
                    f[i][j][idx] = f[i][j - 1][m] + f[i - 1][j][m]

        return f[l - 1][n - 1][0] % mod


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])
        f = [[[0] * k for _ in range(n + 1)] for _ in range(m + 1)]
        f[0][1][0] = f[1][0][0] = 0.5
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                for v in range(k):
                    f[i + 1][j + 1][(v + x) % k] = (f[i + 1][j][v] + f[i][j + 1][v]) % MOD

        return int(f[m][n][0])


