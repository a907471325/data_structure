from typing import List


class Solution:
    # def jewelleryValue(self, frame: List[List[int]]) -> int:
    #     # f[i][j] 定义为从起点->[i, j] 获取的最高价值
    #     # f[i][j] = max(f[i-1][j], f[i][j-1]) + frame[i][j]

    #     m, n = len(frame), len(frame[0])
    #     f = [[0] * n for i in range(m)]

    #     for i in range(m):
    #         for j in range(n):
    #             if i == 0 and j == 0:
    #                 f[i][j] = frame[i][j]
    #             elif i == 0:
    #                 f[i][j] = f[i][j-1] + frame[i][j]
    #             elif j == 0:
    #                 f[i][j] = f[i-1][j] + frame[i][j]
    #             else:
    #                  f[i][j] = max(f[i-1][j], f[i][j-1]) + frame[i][j]
    #     return f[m-1][n-1]

    # 优化空间
    def jewelleryValue(self, frame: List[List[int]]) -> int:
        # f[i][j] 定义为从起点->[i, j] 获取的最高价值
        # f[i][j] = max(f[i-1][j], f[i][j-1]) + frame[i][j]

        m, n = len(frame), len(frame[0])
        f = [0] * n

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    f[j] = frame[i][j]
                elif i == 0:
                    f[j] = f[j - 1] + frame[i][j]
                elif j == 0:
                    f[j] = f[j] + frame[i][j]
                else:
                    f[j] = max(f[j], f[j - 1]) + frame[i][j]
        return f[n - 1]


