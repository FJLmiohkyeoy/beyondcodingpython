N, M, V = map(int, input().split())
graph = [[0] * (N + 1) for i in range(N + 1)]

bfsVisited = [0] * (N + 1)
dfsVisited = [0] * (N + 1)


for i in range(M):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1


def bfs(V):

    queue = [V]
    bfsVisited[V] = 1
    while queue:
        V = queue.pop(0)
        for i in range(N + 1):
            if graph[V][i] == 1 and bfsVisited[i] != 1:
                queue.append(i)
                bfsVisited[i] = 1


def dfs(V):
    dfsVisited[V] = 1
    for i in range(N+1):
        if graph[V][i] == 1 and dfsVisited[i] != 1:
            dfs(i)


dfs(V)
