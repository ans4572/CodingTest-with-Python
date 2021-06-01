T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    temp = list(map(int, input().split()))

    dp = []
    index = 0
    for i in range(n):
        dp.append(temp[index:index + m])
        index += m

    # 오른쪽 가면서 점화식 적용
    for i in range(1, m):
        for j in range(n):
            if j == 0:
                dp[j][i] = max(dp[j][i-1], dp[j+1][i-1]) + dp[j][i]
            elif j == n-1:
                dp[j][i] = max(dp[j-1][i-1], dp[j][i-1]) + dp[j][i]
            else:
                dp[j][i] = max(dp[j - 1][i - 1], dp[j][i-1], dp[j + 1][i - 1]) + dp[j][i]

    #최대 값 찾기
    ans = 0
    for i in range(n):
        ans = max(ans, dp[i][m-1])
    print(ans)

