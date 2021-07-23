from collections import deque

N = int(input())  # 보드의 크기
K = int(input())  # 사과의 개수

board = [[0] * (N + 1) for _ in range(N + 1)]  # 0:빈 공간, 1:뱀 2:사과
for i in range(K):
    row, col = list(map(int, input().split()))
    board[row][col] = 2

L = int(input())
command = []
for i in range(L):
    x, dic = list(input().split())
    command.append((x, dic))
command_idx = 0

# 오른쪽, 아래, 왼쪽, 위 순서
dic = [[0, 1], [1, 0], [0, -1], [-1, 0]]

count = 0
board[1][1] = 1
snake = deque() # 뱀 몸통 위치 deque
snake.append((1,1))
d = 0  # 방향 (처음에는 ->)
while True:
    """
    print()
    for i in range(1, N+1):
        for j in range(1, N+1):
            print(board[i][j], end = " ")
        print()
    """

    count += 1

    # 다음 위치
    next_r = snake[-1][0] + dic[d][0]
    next_c = snake[-1][1] + dic[d][1]
    snake.append((next_r, next_c))

    # 벽에 부딪히는 경우
    if next_r < 1 or next_r > N or next_c < 1 or next_c > N:
        break
    # 뱀을 만나는 경우
    if board[next_r][next_c] == 1:
        break
    # 빈 공간인 경우
    elif board[next_r][next_c] == 0:
        board[snake[0][0]][snake[0][1]] = 0
        snake.popleft()
    board[next_r][next_c] = 1

    # 방향 전환
    if count == int(command[command_idx][0]):
        if command[command_idx][1] == 'D':
            d = (d + 1) % 4
        else:
            d = (d + 3) % 4
        if command_idx < len(command) - 1:
            command_idx += 1

print(count)
