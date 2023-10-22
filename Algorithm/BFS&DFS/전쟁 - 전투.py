N, M = map(int, input().split())
graph = []
for i in range(M):
    graph.append([_ for _ in input()])

wScore = 0
bScore = 0

for x in range(M):
    for y in range(N):

        if graph[x][y] != 'x':
            queue = [[x, y]]
            letter = graph[x][y]
            graph[x][y] = 'x'

            c = 0
            while queue:
                i, j = queue.pop(0)
                if i < M-1 and letter == graph[i+1][j]:
                    queue.append([i+1, j])
                    graph[i+1][j] = 'x'
                if j < N-1 and letter == graph[i][j+1]:
                    queue.append([i, j+1])
                    graph[i][j+1] = 'x'
                if i > 0 and letter == graph[i-1][j]:
                    queue.append([i-1, j])
                    graph[i-1][j] = 'x'
                if j > 0 and letter == graph[i][j-1]:
                    queue.append([i, j-1])
                    graph[i][j-1] = 'x'
                c += 1

            if letter == "w":
                wScore += c**2
            else:
                bScore += c**2

print(wScore, bScore)
