class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # f[i][j] = f[i-1][j], f[i][j-1]

        f = [0] * n

        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    f[j] = 1
                elif i == 0:
                    f[j] = f[j - 1]
                elif j == 0:
                    f[j] = f[j]
                else:
                    f[j] = f[j] + f[j - 1]
        return f[n - 1]

