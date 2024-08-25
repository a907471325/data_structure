class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        max_val = 1e9
        m = len(matrix)
        n = len(matrix[m - 1])

        f = [[0] * n for i in range(2)]

        for j in range(n):
            f[0][j] = matrix[0][j]

        for i in range(1, m):
            for j in range(n):
                left = f[(i - 1) % 2][j - 1] if j > 0 else max_val
                mid = f[(i - 1) % 2][j]
                right = f[(i - 1) % 2][j + 1] if j < n - 1 else max_val

                f[i % 2][j] = min(left, right, mid) + matrix[i][j]

        return min(f[(m - 1) % 2])

