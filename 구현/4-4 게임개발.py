N, M = map(int, input().split())

visit = [[0]*M for _ in range(N)]    # N * M 2차원 배열 생성

A, B, dir = map(int, input().split())   # 현재 위치와 방향 입력
visit[A][B] = 1                      # 현재 위치 방문 표시

# 맵 정보 입력
array = []
for _ in range(N):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]
count = 1

while True:
    moved = False
    # 1,2단계 수행
    for d in range(1, 4):
        nd = (4 + dir - d) % 4  # 왼쪽 방향으로 전환
        nx = A+dx[nd]
        ny = B+dy[nd]
        # 이동할 수 있는 조건을 판단하여 이동
        if nx >= 0 and nx < N and ny >=0 and ny < M and array[nx][ny] == 0 and visit[nx][ny] == 0:
            dir = nd
            A = nx
            B = ny
            visit[nx][ny] = 1
            moved = True
            count += 1
            break

    # 3단계
    if moved == False:
        bx = A - dx[dir]
        by = B - dy[dir]
        if array[bx][by] == 1:
            break
        else:
            A = bx
            B = by

print(count)