N, M = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)

ans = 0
while start <= end:
    mid = (start + end) // 2

    sum = 0
    for i in arr:
        if i > mid:
            sum += i - mid

    if sum < M:
        end = mid - 1
    else:
        ans = mid
        start = mid + 1

print(ans)