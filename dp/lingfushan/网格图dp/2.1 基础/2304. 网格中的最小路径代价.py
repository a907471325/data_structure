class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:


        max_val = 1e9
        m = len(grid)
        n = len(grid[m - 1])

        f = [[0] * n for i in range(2)]
        for j in range(n):
            f[0][j] = grid[0][j]

        for i in range(1, m):
            for j in range(n):
                min_val = 1e9
                for x, val in enumerate(grid[i-1]):
                    min_val = min(f[(i - 1) % 2][x] + moveCost[val][j], min_val)

                f[i % 2][j] = min_val + grid[i][j]


        return min(f[(m - 1) % 2])


