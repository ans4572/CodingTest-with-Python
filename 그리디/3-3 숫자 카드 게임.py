N,M = map(int,input().split())

ans = 0
for i in range(N):
    row = map(int,input().split())
    ans = max(ans, min(row))

print(ans)