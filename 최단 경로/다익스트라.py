import heapq

# 노드 개수와 간선 개수
n, m = map(int, input().split())
# 시작 노드 번호
start = int(input())
# 그래프 리스트
graph = [[] for i in range(n+1)]
distance = [float('inf')] * (n+1)
# 간선 입력 받기
for i in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

#다익스트라 알고리즘
def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q,(0, start))
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == float('inf'):
        print('none')
    else:
        print(distance[i])



