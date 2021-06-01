from collections import deque

N,M = map(int,input().split())

graph = []
for i in range(N):
    graph.append(list(map(int,input())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def BFS(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

BFS(0,0)
print(graph[N-1][M-1])