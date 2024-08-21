MOD = 10 ** 9 + 7


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        # f[i][j]为从00 ->ij 的最大乘积
        # f[i][j] 分情况讨论
        #  1. g[i][j] 为正数, f[i][j] = max(f[i-1][j], f[i][j-1]) * g[i][j]
        #  2. g[i][j] 为负数  f[i][j] = min(f[i-1][j], f[i][j-1]) * g[i][j]
        # 所以既要保存f[i-1][j], f[i][j-1]的最大值，也要保存最小值

        m, n = len(grid), len(grid[0])

        f_max = [[-1e9] * n for i in range(m)]
        f_min = [[1e9] * n for i in range(m)]
        f_max[0][0], f_min[0][0] = grid[0][0], grid[0][0]

        for i in range(1, m):
            f_max[i][0], f_min[i][0] = f_max[i - 1][0] * grid[i][0], f_min[i - 1][0] * grid[i][0]

        for j in range(1, n):
            f_max[0][j], f_min[0][j] = f_max[0][j - 1] * grid[0][j], f_min[0][j - 1] * grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] > 0:
                    f_max[i][j] = max(f_max[i - 1][j], f_max[i][j - 1]) * grid[i][j]
                    f_min[i][j] = min(f_min[i - 1][j], f_min[i][j - 1]) * grid[i][j]
                elif grid[i][j] < 0:
                    f_max[i][j] = min(f_min[i - 1][j], f_min[i][j - 1]) * grid[i][j]
                    f_min[i][j] = max(f_max[i - 1][j], f_max[i][j - 1]) * grid[i][j]
                else:
                    f_max[i][j] = 0
                    f_min[i][j] = 0

        return -1 if f_max[m - 1][n - 1] < 0 else f_max[m - 1][n - 1] % MOD

