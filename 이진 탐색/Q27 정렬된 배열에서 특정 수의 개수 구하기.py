from bisect import bisect_left, bisect_right

N, x = map(int, input().split())
arr = list(map(int, input().split()))

left_index = bisect_left(arr, x)
right_index = bisect_right(arr, x)

if right_index - left_index == 0:
    print(-1)
else:
    print(right_index - left_index)

