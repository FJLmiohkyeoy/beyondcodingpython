import sys

input = sys.stdin.readline

N = int(input())

train = tuple(map(int, input().split()))

m = int(input())

dp = [[0] * 3 for _ in range(N)]

v = 0
s = [0] + [v := v + t for t in train]

for i in range(m):
    dp[i][0] = s[i + 1]

for i in range(m, N):

    dp[i][0] = max(s[i + 1] - s[i + 1 - m], dp[i - 1][0])

    for j in range(1, 3):
        dp[i][j] = max(dp[i - 1][j], dp[i - m][j - 1] + (s[i + 1] - s[i + 1 - m]))

print(dp[-1][-1])
