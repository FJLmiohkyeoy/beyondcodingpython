import sys

input = sys.stdin.readline

N = int(input())

dp = [0, 1, 2, 3, 4, 5]
for i in range(6, N + 1):
    dp.append(max(dp[i - 3] * 2, dp[i - 4] * 3, dp[i - 5] * 4))

print(dp[N])
