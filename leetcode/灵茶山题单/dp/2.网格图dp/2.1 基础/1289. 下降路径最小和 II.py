class Solution:
    # n ^ 3
    # def minFallingPathSum(self, grid: List[List[int]]) -> int:

    #     max_val = 1e9
    #     m = len(grid)
    #     n = len(grid[m - 1])

    #     f = [[0] * n for i in range(2)]

    #     for j in range(n):
    #         f[0][j] = grid[0][j]

    #     for i in range(1, m):
    #         for j in range(n):
    #             left = min(f[(i - 1) % 2][:j]) if j > 0 else max_val
    #             # mid = f[(i - 1) % 2][j]
    #             right = min(f[(i - 1) % 2][j+1:]) if j < n -1 else max_val

    #             f[i % 2][j] = min(left, right) + grid[i][j]

    #     return min(f[(m - 1) % 2])

    # n ^ 2
    def minFallingPathSum(self, grid: List[List[int]]) -> int:

        max_val = 1e9
        m = len(grid)
        n = len(grid[m - 1])

        f = [[0] * n for i in range(2)]

        min_1, min_2 = -1, -1
        for j in range(n):
            f[0][j] = grid[0][j]

            if (grid[0][min_1] if min_1 != -1 else max_val )> grid[0][j]:
                min_2 = min_1
                min_1 = j
            elif (grid[0][min_2] if min_2 != -1 else max_val) > grid[0][j]:
                min_2 = j

        for i in range(1, m):
            t_1, t_2 = -1, -1
            for j in range(n):
                cur_min = f[(i - 1) % 2][min_2] if j == min_1 else  f[(i - 1) % 2][min_1]
                # left = min(f[(i - 1) % 2][:j]) if j > 0 else max_val
                # # mid = f[(i - 1) % 2][j]
                # right = min(f[(i - 1) % 2][j+1:]) if j < n -1 else max_val

                f[i % 2][j] = cur_min + grid[i][j]

                if (f[i % 2][t_1] if t_1 != -1 else max_val) > f[i % 2][j]:
                    t_2 = t_1
                    t_1 = j
                elif (f[i % 2][t_2] if t_2 != -1 else max_val) > f[i % 2][j]:
                    t_2 = j

            min_1 = t_1
            min_2 = t_2

        return min(f[(m - 1) % 2])



