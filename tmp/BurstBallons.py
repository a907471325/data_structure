
nums = [3,1,5,8]
n = len(nums)
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    l = 1 if i == 0 else nums[i - 1]
    r = 1 if i == n - 1 else nums[i + 1]
    dp[i][i] = l * nums[i] * r

for i in range(n - 2, -1, -1):
    for j in range(i + 1, n):
        for k in range(i, j + 1):

            if k == i:
                l = 1 if k - 1 < 0 else nums[k - 1]
                r = 1 if j + 1 > n - 1 else nums[j + 1]
                dp[i][j] = max(l * nums[k] * r + dp[i + 1][j], dp[i][j])
            if k == j:
                l = 1 if i - 1 < 0 else nums[i - 1]
                r = 1 if k + 1 > n - 1 else nums[k + 1]
                dp[i][j] = max(l * nums[k] * r + dp[i][j - 1], dp[i][j])
            if i < k and k < j:
                l = 1 if i - 1 < 0 else nums[i - 1]
                r = 1 if j + 1 > n - 1 else nums[j + 1]
                dp[i][j] = max(l * nums[k] * r + dp[i][k - 1] + dp[k + 1][j], dp[i][j])

print (dp[0][n - 1])
