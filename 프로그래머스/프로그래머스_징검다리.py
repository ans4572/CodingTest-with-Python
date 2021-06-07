def solution(distance, rocks, n):
    rocks.append(0)
    rocks.append(distance)
    rocks.sort()

    arr = []       #간격 저장
    for idx in range(1, len(rocks)):
        arr.append(rocks[idx] - rocks[idx - 1])

    answer = 0
    left = 0
    right = distance
    while left <= right:
        mid = (left + right) // 2
        jump, count = 0, 0    #jump: 점프 거리, count: 점프 횟수
        for i in arr:
            jump += i
            if jump >= mid:
                jump = 0
                count += 1

        if count <= len(rocks) - 2 - n:
            right = mid - 1
        else:
            left = mid + 1
            answer = max(answer, mid)

    return answer

print(solution(25, [2,14,11,21,17], 2))