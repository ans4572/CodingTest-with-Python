N,K = map(int,input().split())

ans = 0
while True:
    temp = N % K
    ans += temp
    N -= temp

    if N < K:
        break

    ans += 1
    N //= K

ans += N - 1
print(ans)