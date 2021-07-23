def rotation(arr, x1, y1, x2, y2):
    temp = arr[x1][y1]
    min_num = temp
    h = x2 - x1
    w = y2 - y1
    for i in range(h):
        arr[x1 + i][y1] = arr[x1 + i + 1][y1]
        min_num = min(min_num, arr[x1 + i][y1])
    for i in range(w):
        arr[x2][y1 + i] = arr[x2][y1 + i + 1]
        min_num = min(min_num, arr[x2][y1 + i])
    for i in range(h):
        arr[x2 - i][y2] = arr[x2 - i - 1][y2]
        min_num = min(min_num, arr[x2 - i][y2])
    for i in range(w - 1):
        arr[x1][y2 - i] = arr[x1][y2 - i - 1]
        min_num = min(min_num, arr[x1][y2 - i])
    arr[x1][y1 + 1] = temp

    return min_num


def solution(rows, columns, queries):
    arr = [[0] * 101 for _ in range(101)]
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            arr[i][j] = ((i - 1) * columns + j)

    answer = []
    for i in range(len(queries)):
        answer.append(rotation(arr, queries[i][0], queries[i][1], queries[i][2], queries[i][3]))

    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
print(solution(100, 97, [[1,1,100,97]]))