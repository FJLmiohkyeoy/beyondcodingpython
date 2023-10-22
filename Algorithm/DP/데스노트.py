import sys

input = sys.stdin.readline

n, m = map(int, input().split())

names = [int(input()) for _ in range(n)]

MAXNUM = 10000000000000

dp = [[MAXNUM] * (m + 1) for _ in range(n)]

dp[0][names[0]] = 0

for i in range(1, n):
    for j in range(1, m + 1):
        if dp[i - 1][j] == MAXNUM:
            continue

        if j + names[i] + 1 < m + 1:
            dp[i][j + names[i] + 1] = min(
                dp[i][j + names[i] + 1],
                dp[i - 1][j],
            )

        dp[i][names[i]] = min(dp[i][names[i]], dp[i - 1][j] + (m - j) ** 2)

for i in range(m + 1):
    print(str(i).rjust(6, " "), end=" ")
print()
print("-" * 7 * (m + 1))

for d in dp:
    for e in d:
        if e == MAXNUM:
            print("MAXNUM", end=" ")
        else:
            print(str(e).rjust(6, " "), end=" ")
    print()

print(min(dp[-1]))


# import sys

# input = sys.stdin.readline

# n, m = map(int, input().split())

# names = [int(input()) for _ in range(n)]

# MAXNUM = 10000000000000

# dp = [[MAXNUM] * (m + 1) for _ in range(n)]

# dp[0][names[0]] = (m - names[0]) ** 2

# for i in range(1, n):
#     for j in range(1, m + 1):
#         if dp[i - 1][j] == MAXNUM:
#             continue

#         if j + names[i] + 1 < m + 1:
#             dp[i][j + names[i] + 1] = min(
#                 dp[i][j + names[i] + 1],
#                 dp[i - 1][j] - (m - j) ** 2 + (m - (j + names[i] + 1)) ** 2,
#             )

#         dp[i][names[i]] = min(dp[i][names[i]], dp[i - 1][j] + (m - names[i]) ** 2)

# for i in range(1, m + 1):
#     if dp[-1][i] != MAXNUM:
#         dp[-1][i] = dp[-1][i] - (m - i) ** 2

# print(min(dp[-1]))
