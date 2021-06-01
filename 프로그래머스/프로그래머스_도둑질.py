def solution(money):
    size = len(money)

    # dy[n][0]: 첫번째 포함 => 마지막 포함 불가, dy[n][1]: 첫번째 포함 X => 마지막 포함 가능
    dy = [[0] * 2 for _ in range(size)]

    dy[0][0] = money[0]
    dy[0][1] = 0
    dy[1][0] = money[0]
    dy[1][1] = money[1]

    for i in range(2, size - 1):
        dy[i][0] = max(dy[i-1][0], dy[i-2][0] + money[i])
        dy[i][1] = max(dy[i-1][1], dy[i-2][1] + money[i])

    dy[size - 1][1] = max(dy[size - 3][1] + money[size-1], dy[size-2][1])

    return max(dy[size-1][0], dy[size-1][1], dy[size-2][0], dy[size-2][1])

print(solution([1000,1,0,1,2,1000,0]))