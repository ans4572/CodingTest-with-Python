import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
M = int(input())

dist = [0] * (N + 1)    # 지점 a 까지 가는 최대 비용
parent = [0] * (N + 1)  # 루트 저장하기 위한 배열
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    p, q, r = map(int, input().split())
    graph[p].append((q,r))

last = -1
q = deque([[1, 0]])
while q:
    now = q.popleft()
    if now[0] == 1 and now[1] > 0:
        continue

    for next, cost in graph[now[0]]:
        if dist[next] < now[1] + cost:
            if next == 1
                last = now[0]
            dist[next] = now[1] + cost
            parent[next] = now[0]
            q.append((next, now[1] + cost))

print(dist[1])
