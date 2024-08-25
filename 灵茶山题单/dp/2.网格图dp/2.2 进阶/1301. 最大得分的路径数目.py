class Solution:
    # 解法1 先dp求最大路径，在dfs找最大路径出现次数，超时
    # def pathsWithMaxScore(self, board: List[str]) -> List[int]:
    #     # e 2 1
    #     # 2 3 2
    #     # 1 2 s
    #     m,n = len(board), len(board[0])
    #     board[0] = board[0].replace("E", "0")
    #     board[m-1] = board[m-1].replace("S", "0")
    #     f = [[0] * n for _ in range(m)]

    #     for i in range(1, m):
    #         f[i][0] = (f[i-1][0] + int(board[i][0])) if board[i][0] != "X" and f[i-1][0] != -1 else -1

    #     for j in range(1, n):
    #         f[0][j] = (f[0][j-1] + int(board[0][j])) if board[0][j] != "X" and f[0][j-1] != -1 else -1

    #     for i in range(1, m):
    #         for j in range(1, n):
    #             if board[i][j] == "X":
    #                 f[i][j] = -1
    #                 continue
    #             res = -1
    #             cur_val = int(board[i][j])
    #             for d in [(-1, -1), (0, -1), (-1, 0)]:
    #                 xn, yn = i + d[0], j + d[1]
    #                 res = max(res, f[xn][yn] + cur_val)
    #             f[i][j] = res

    #     max_len = f[m-1][n-1]

    #     if max_len == -1:
    #         return [0, 0]

    #     @cache
    #     def dfs(x, y, path):

    #         if x == m-1 and y == n-1:

    #             return 1 if path == 0 else 0

    #         res = 0
    #         for d in [(1, 1), (0, 1), (1, 0)]:
    #             xn, yn = x + d[0], y + d[1]
    #             if xn < m and yn < n and board[xn][yn] != "X":
    #                 res += dfs(xn, yn, path - int(board[xn][yn]))

    #         return res

    #     res = dfs(0,0, max_len)
    #     return [max_len, res % (10**9 + 7)]

    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        # e 2 1
        # 2 3 2
        # 1 2 s
        m, n = len(board), len(board[0])
        board[0] = board[0].replace("E", "0")
        board[m - 1] = board[m - 1].replace("S", "0")
        f = [[0] * n for _ in range(m)]
        g = [[0] * n for _ in range(m)]
        g[0][0] = 1

        for i in range(1, m):
            f[i][0] = (f[i - 1][0] + int(board[i][0])) if board[i][0] != "X" and f[i - 1][0] != -1 else -1
            g[i][0] = g[i - 1][0] if board[i][0] != "X" else 0

        for j in range(1, n):
            f[0][j] = (f[0][j - 1] + int(board[0][j])) if board[0][j] != "X" and f[0][j - 1] != -1 else -1
            g[0][j] = g[0][j - 1] if board[0][j] != "X" else 0

        for i in range(1, m):
            for j in range(1, n):
                if board[i][j] == "X":
                    f[i][j] = -1
                    g[i][j] = 0
                    continue

                lens = []
                cnts = []
                cur_val = int(board[i][j])
                for d in [(-1, -1), (0, -1), (-1, 0)]:
                    xn, yn = i + d[0], j + d[1]
                    lens.append(f[xn][yn] + cur_val)
                    cnts.append(g[xn][yn])

                max_len = max(lens)

                cnt = 0
                for idx, l in enumerate(lens):
                    if l == max_len and l != -1:
                        cnt += cnts[idx]

                res = max_len

                f[i][j] = res
                g[i][j] = cnt

        max_len = f[m - 1][n - 1]

        if max_len == -1:
            return [0, 0]

        return [max_len, cnt % (10 ** 9 + 7)]
