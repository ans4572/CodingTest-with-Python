def DFS(graph, n, visited):
    visited[n] = True  #방문 표시
    print(n, end=' ')
    for i in graph[n]:
        if not visited[i]:
            visited[i] = True
            DFS(graph, i, visited)

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

DFS(graph, 1, visited)