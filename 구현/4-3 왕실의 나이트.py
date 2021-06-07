location = input()
x = int(ord(location[0])) - int(ord('a')) + 1
y = int(location[1])

step = [(-2,-1), (-2,1), (-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2)]

ans = 0
for dx,dy in step:
    nx = x + dx
    ny = y + dy
    if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
        ans += 1

print(ans)