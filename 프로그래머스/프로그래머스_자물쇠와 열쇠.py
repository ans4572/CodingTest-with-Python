# _*_ coding: utf-8 _*_
from __future__ import print_function

# 90도 회전하여 반환
def rotation(key, m):
    rotated_key = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            rotated_key[i][j] = key[j][m - i - 1]
    return rotated_key

# board에 key 삽입하여 확인
def insert_key(board, key, i, j, n, m):
    is_possible = True

    for x in range(i, m + i):
        for y in range(j, m + j):
            board[x][y] += key[x - i][y - j]

    # lock 부분이 전부 1로 되어 있나 확인
    for x in range(m, n + m):
        for y in range(m, n + m):
            if board[x][y] != 1:
                is_possible = False

    for x in range(i, m + i):
        for y in range(j, m + j):
            board[x][y] -= key[x - i][y - j]

    return is_possible

# key를 순서대로 넣어보고 가능한 경우가 있다면 True를 반환
def insert_keys(board, key, n, m):
    is_possible = False

    for i in range(n + m):
        for j in range(n + m):
           if insert_key(board, key, i, j, n, m):
               is_possible = True

    return is_possible

def solution(key, lock):
    n, m = len(lock), len(key)
    board = [[0] * (n + 2 * m) for _ in range(n + 2 * m)]

    # 가운데에 lock 넣기
    for i in range(m, m + n):
        for j in range(m, m + n):
            board[i][j] = lock[i - m][j - m]

    # 4번 실행
    for _ in range(4):
        if insert_keys(board, key, n, m):
            return True
        key = rotation(key, m)

    return False

print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]]))