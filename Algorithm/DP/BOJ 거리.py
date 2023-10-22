import sys

input = sys.stdin.readline

N = int(input())
blocks = input().strip()


dp = [N**2] * N

dp[0] = 0

prevBlock = {"B": "J", "O": "B", "J": "O"}

for i in range(N):
    for j in range(i):
        if blocks[j] == prevBlock[blocks[i]]:
            dp[i] = min(dp[i], dp[j] + (i - j) ** 2)

if dp[-1] == N**2:
    print(-1)
else:
    print(dp[-1])
