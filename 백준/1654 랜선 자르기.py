K, N = map(int, input().split())
arr = []
for i in range(K):
    arr.append(int(input()))

left = 0
right = max(arr)

ans = 0
while left <= right:
    mid = (left + right) // 2
    count = 0
    for i in arr:
        count += (i // mid)

    if count < N:
        right = mid - 1
    else:
        ans = max(ans, mid)
        left = mid + 1

print(ans)