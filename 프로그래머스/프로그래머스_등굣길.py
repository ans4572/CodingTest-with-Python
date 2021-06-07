def solution(m, n, puddles):
    dy = [[0]*(m + 1) for _ in range(n + 1)]

    for pos in puddles:
        dy[pos[1]][pos[0]] = -1

    dy[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == j == 1:
                continue
            # 물인 경우 0으로 만들어서 다음 계산에 영향 X
            if dy[i][j] == -1:
                dy[i][j] = 0
                continue
            dy[i][j] = (dy[i-1][j] + dy[i][j-1]) % 1000000007

    return dy[n][m]

solution(4, 3, [])