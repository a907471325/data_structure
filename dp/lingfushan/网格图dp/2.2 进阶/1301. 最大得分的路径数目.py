from typing import List


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        # e 2 3
        # 2 x 2
        # 1 2 s
        res = [0, 0]
        m, n = len(board), len(board[0])

        def dfs(x, y, path):
            if board[x][y] == "S":
                if path > res[0]:
                    res[0] = path
                    res[1] = 1
                elif path == res[0]:
                    res[1] += 1
                return

            for d in [(1, 1), (0, 1), (1, 0)]:
                xn, yn = x + d[0], y + d[0]
                if xn < m and yn < n and board[xn][yn] != "X":
                    dfs(xn, yn, path + int(board[xn][yn]))

        dfs(0, 0, 0)
        res[1] = res[1] % (10 ** 9 + 7)
        return res


if __name__ == '__main__':
    board = ["E23","2X2","12S"]
    so = Solution()
    so.pathsWithMaxScore(board)


