def solution(game_board, table):

    # 90도 회전 함수
    def rotation(table):
        N = len(table)
        ret = [[0] * N for _ in range(N)]

        for i in range(N):
            for j in range(N):
                ret[j][N-1-i] = table[i][j]

        return ret

    # board의 크기를 3배로 확장하고 중앙 부분에 기존의 board 넣기
    N = len(game_board)
    new_board = [[2] * (N * 3) for _ in range(N * 3)]  # 벽이라면 2
    for i in range(N):
        for j in range(N):
            if game_board[i][j] == 1:
                new_board[i + N][j + N] = 2
            else:
                new_board[i + N][j + N] = 0

    # board에 블록 넣기를 4번을 진행
    for r in range(4):
        table = rotation(table)

        for x in range(N * 2):
            for y in range(N * 2):
                # 끼워 넣기
                for i in range(N):
                    for j in range(N):
                        new_board[x+i][y+j] += table[i][j]

        rotation(table)  # table 회전 진행

    answer = -1
    return answer