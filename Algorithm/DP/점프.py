import sys
input = sys.stdin.readline

N = int(input())

board = [[x for x in map(int, input().split())] for _ in range(N)]

dp = [[0] * N for _ in range(N)]

dp[0][0] = 1
for i in range(N):
    for j in range(N):
        d = dp[i][j]
        b = board[i][j]
        if b:
            if j + b < N:
                dp[i][j + b] += d
            if i + b < N:
                dp[i + b][j] += d

print(dp[-1][-1])


# queue = [[0, 0]]
# c = 0
# while queue:
#     n, m = queue.pop(0)

#     if n == N - 1 and m == N - 1:
#         c += 1
#         continue

#     if board[n][m] == 0:
#         continue

#     mx = m + board[n][m]
#     nx = n + board[n][m]

#     if mx < N:
#         queue.append([n, mx])
#     if nx < N:
#         queue.append([nx, m])

# print(c)
