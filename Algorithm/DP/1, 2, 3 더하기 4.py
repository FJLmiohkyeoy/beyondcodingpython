import sys

input = sys.stdin.readline

T = int(input())
nums = [int(input()) for _ in range(T)]

m = max(nums)
dp = [[0, 0], [1, 0], [1, 1]]
for i in range(3, m):
    dp.append([dp[i - 2][0] + 1, dp[i - 3][0] + dp[i - 3][1] + 1])

for n in nums:
    print(dp[n - 1][0] + dp[n - 1][1] + 1)
