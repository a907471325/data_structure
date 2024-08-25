class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        # f[i][j] 定义为从起点->[i, j] 获取的最高价值
        # f[i][j] = max(f[i-1][j], f[i][j-1]) + frame[i][j]

        m, n = len(grid), len(grid[0])
        f = [0] * n

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    f[j] = grid[i][j]
                elif i == 0:
                    f[j] = f[j - 1] + grid[i][j]
                elif j == 0:
                    f[j] = f[j] + grid[i][j]
                else:
                    f[j] = min(f[j], f[j - 1]) + grid[i][j]
        return f[n - 1]

