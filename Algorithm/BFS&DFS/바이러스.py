x = int(input())
graph = [[0] * (x+1) for _ in range(x+1)]
visited = [0] * (x+1)
y = int(input())

for _ in range(y):
    i, j = map(int, input().split())
    graph[i][j] = graph[j][i] = 1

queue = [1]
visited[1] = 1
c = 0
while queue:
    a = queue.pop(0)
    for j in range(x+1):
        if graph[a][j] == 1 and visited[j] != 1:
            queue.append(j)
            visited[j] = 1
            c += 1

print(c)
