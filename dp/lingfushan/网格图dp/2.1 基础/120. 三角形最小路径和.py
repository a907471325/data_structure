class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:


        m = len(triangle)
        n = len(triangle[m-1])

        f =[[0] * n for i in range(2)]
        f[0][0] = triangle[0][0]


        for i in range(1, m):
            f[i % 2][0] = f[(i-1) % 2][0] + triangle[i][0]
            for j in range(1, len(triangle[i])):
                if j == len(triangle[i]) - 1:
                    f[i % 2][j] = f[(i-1) % 2][j-1] + triangle[i][j]
                else:
                    f[i % 2][j] = min(f[(i-1) % 2][j], f[(i-1) % 2][j-1]) + triangle[i][j]

        return min(f[(m - 1)% 2])

