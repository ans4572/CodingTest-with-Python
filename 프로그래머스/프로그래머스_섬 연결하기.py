import heapq

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a != b:
        if a > b:
            parent[a] = b
        else:
            parent[b] = a

def solution(n, costs):
    heap = []

    for a, b, c in costs:
        heapq.heappush(heap, (c, a, b))

    answer = 0
    parent = []
    for i in range(n):
        parent.append(i)

    while heap:
        cost, a, b = heapq.heappop(heap)

        if find(parent, a) == find(parent, b):
            continue
        else:
            union(parent, a, b)
            answer += cost

    return answer

print(solution(5, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]]))