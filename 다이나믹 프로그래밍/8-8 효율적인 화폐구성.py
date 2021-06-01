N, M = map(int, input().split())
money = []
for i in range(N):
    money.append(int(input()))

dp = [10001] * (M + 1)
dp[0] = 0

for i in range(N):
    for j in range(money[i], M + 1):
        dp[j] = min(dp[j], dp[j - money[i]] + 1)

if dp[M] == 10001:
    print(-1)
else:
    print(dp[M])