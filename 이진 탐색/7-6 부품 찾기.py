def binary_search(arr, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        else:
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

    return False

N = int(input())
arr = list(map(int,input().split()))
arr.sort()
M = int(input())
targets = list(map(int,input().split()))

for i in targets:
    if binary_search(arr, i, 0, N-1):
        print('yes', end=' ')
    else:
        print('no', end=' ')