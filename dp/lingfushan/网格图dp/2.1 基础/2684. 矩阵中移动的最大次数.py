class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[m - 1])

        cache = []
        res = [0]

        def dfs(x, y):
            res[0] = max(y, res[0])
            if y == n - 1:
                return

            if x - 1 >= 0 and grid[x - 1][y + 1] > grid[x][y]:
                dfs(x - 1, y + 1)
            if x + 1 < m and grid[x + 1][y + 1] > grid[x][y]:
                dfs(x + 1, y + 1)
            if grid[x][y + 1] > grid[x][y]:
                dfs(x, y + 1)
            grid[x][y] = 0

        for i in range(m):
            dfs(i, 0)

        return res[0]


