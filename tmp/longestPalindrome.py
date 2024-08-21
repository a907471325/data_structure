s = "babad"
s = "aacabdkacaa"

n = len(s)
dp = [[False for _ in range(n)] for _ in range(n)]
max_len = 0
start_idx = 0
for i in range(n):
    dp[i][i] = True

for i in range(n - 2, -1, -1):
    for j in range(i + 1, n):

        if s[i] == s[j]:
            if j - i == 1:
                dp[i][j] = True
            else:
                dp[i][j] = dp[i + 1][j - 1]
            if j - i > max_len:
                max_len = j - i + 1
                start_idx = i

print(s[start_idx: start_idx + max_len])

