import sys
input = sys.stdin.readline

N = int(input())
T = []
P = []
dp = [0] * (N+1)
for _ in range(N):
    ti, pi = map(int, input().split())
    T.append(ti)
    P.append(pi)

for i in range(N):
    dp[i+1] = max(dp[i], dp[i+1])

    if i + T[i] > N:
        continue

    dp[i+T[i]] = max(dp[i+T[i]], dp[i] + P[i])

print(dp[-1])
