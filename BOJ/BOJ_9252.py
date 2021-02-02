import sys
input = sys.stdin.readline
x = [0] + list(input().strip())
y = [0] + list(input().strip())
len_x = len(x)
len_y = len(y)
dp = [[""] * len_y for i in range(len_x)]
for i in range(1, len_x):
    for j in range(1, len_y):
        if x[i] == y[j]:
            dp[i][j] = dp[i - 1][j - 1] + x[i]
        else:
            if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]
print(len(dp[len_x - 1][len_y - 1]))
print(dp[len_x - 1][len_y - 1])