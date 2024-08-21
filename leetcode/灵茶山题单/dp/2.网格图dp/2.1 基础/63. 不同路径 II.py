class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:


        # f[i][j] = f[i-1][j], f[i][j-1]

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        f = [0] * n

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    f[j] = 0
                    continue

                if i == 0 and j == 0:
                    f[j] = 1
                elif i == 0:
                    f[j] = f[j - 1]
                elif j == 0:
                    f[j] = f[j]
                else:
                    f[j] = f[j] + f[j - 1]
        return f[n - 1]

