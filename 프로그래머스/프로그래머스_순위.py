# _*_ coding: utf-8 _*_

def solution(n, results):
    graph = [[''] * n for _ in range(n)]

    # graph 세팅
    for i in range(n):
        graph[i][i] = 'D'
    for w, l in results:
        graph[w-1][l-1] = 'W'
        graph[l-1][w-1] = 'L'

    # 플로이드-와샬
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] == 'W' and graph[k][j] == 'W':
                    graph[i][j] = 'W'
                if graph[i][k] == 'L' and graph[k][j] == 'L':
                    graph[i][j] = 'L'

    answer = 0

    for i in range(n):
        if '' not in graph[i]:
            answer += 1

    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))