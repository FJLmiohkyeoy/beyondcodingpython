import sys

input = sys.stdin.readline

N, K = map(int, input().split())

stuff = [list(map(int, input().split())) for _ in range(N)]

# 2차원 DP
dp = [[-1] * (K + 1) for _ in range(N + 1)]

dp[0][0] = 0

for i in range(1, N + 1):

    for j in range(K + 1):

        if dp[i - 1][j] < 0:
            continue

        if dp[i - 1][j] > dp[i][j]:
            dp[i][j] = dp[i - 1][j]

        if stuff[i - 1][0] + j < K + 1:
            dp[i][j + stuff[i - 1][0]] = max(
                dp[i][j + stuff[i - 1][0]], stuff[i - 1][1] + dp[i - 1][j]
            )

print(max(dp[-1]))
