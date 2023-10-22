N, M, K = map(int, input().split())

hallway = [[0] * M for _ in range(N)]

trashes = []

for _ in range(K):

    r, c = map(int, input().split())
    trashes.append([r-1, c-1])
    hallway[r-1][c-1] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = []
sizeOfTrashes = []

while trashes:
    y, x = trashes.pop(0)
    queue.append([y, x])
    hallway[y][x] = 0

    c = 1
    while queue:
        y, x = queue.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx > M - 1 or ny > N - 1:
                continue

            if hallway[ny][nx] != 1:
                continue

            queue.append([ny, nx])
            hallway[ny][nx] = 0
            trashes.pop(trashes.index([ny, nx]))

            c += 1
    sizeOfTrashes.append(c)

print(max(sizeOfTrashes))
