N,M = map(int,input().split())

graph = []
for i in range(N):
    graph.append(list(map(int,input())))

print(graph)

def DFS(x,y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return
    if graph[x][y] == 0:
        graph[x][y] = 1
        DFS(x-1,y)
        DFS(x+1,y)
        DFS(x,y-1)
        DFS(x,y+1)
    return

ans = 0
for i in range(N):
    for j in range(M):
        # 0인 경우 DFS실행
        if graph[i][j] == 0:
            DFS(i,j)
            ans += 1

print(ans)