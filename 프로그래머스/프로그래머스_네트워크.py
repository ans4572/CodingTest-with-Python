def Find(x, parent):
    if x != parent[x]:
        parent[x] = Find(parent[x], parent)
    return parent[x]

def Union(x, y, parent):
    x = Find(x, parent)
    y = Find(y, parent)
    if x != y:
        if x > y: parent[x] = y
        else: parent[y] = x

def solution(n, computers):
    parent = []
    for i in range(n):
        parent.append(i)

    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                Union(i, j, parent)

    parent = [Find(val, parent) for val in parent]

    case = set(parent)

    return len(case)

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))