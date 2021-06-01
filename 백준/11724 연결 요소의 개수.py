N, M = map(int, input().split())
parent = []
for i in range(N+1):
    parent.append(i)

# Union-Find 활용
def Find(x):
    if parent[x] == x:
        return x
    else:
        return Find(parent[x])

def Union(x, y):
    x = Find(x)
    y = Find(y)
    if x != y:
        if x > y:
            parent[x] = y
        else:
            parent[y] = x

for _ in range(M):
    a, b = map(int, input().split())
    Union(a, b)

result = []
for i in parent:
    result.append(Find(i))

print(len(set(result[1:])))