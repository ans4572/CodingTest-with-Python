N = int(input())
plan = input().split()
X, Y = 1, 1

# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
moves = ['L','R','U','D']

for p in plan:
    for i in range(len(moves)):
        if p == moves[i]:
            X += dx[i]
            Y += dy[i]
        # 범위를 벗어나는 경우 다시 원래대로 복구
        if X < 1 or X > N or Y < 1 or Y > N:
            X -= dx[i]
            Y -= dy[i]

print(X,Y)