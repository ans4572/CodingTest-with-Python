def solution(N):
    coin = [500,100,50,10]

    ans = 0
    for i in coin:
        ans += N // i
        N = N % i

    return ans

print(solution(1260))