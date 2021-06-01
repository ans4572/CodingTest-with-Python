def solution(N, M, K):
    data = list(map(int, input().split()))

    data.sort()
    first = data[N-1]
    second = data[N-2]

    ans = 0

    while True:
        for i in range(K):
            ans += first
            M -= 1
            if M == 0:
                break
        ans += second
        M -= 1

        if M == 0:
            break

    return ans

print(solution(5,8,3))