# _*_ coding: utf-8 _*_

def DFS(queen, row, n):
    if row == n:
        return 1

    count = 0

    for num in range(n):
        queen[row] = num

        for i in range(row):
            # 이미 나온 수 인 경우
            if queen[i] == num:
                break
            # 대각선인 경우
            if abs(queen[i] - num) == row - i:
                break

        else:
            count += DFS(queen, row + 1, n)

    return count

def solution(n):
    return DFS([0] * n, 0, n)

print(solution(4))