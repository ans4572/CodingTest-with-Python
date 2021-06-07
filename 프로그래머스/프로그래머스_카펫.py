def solution(brown, yellow):
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            j = yellow // i
            if (i+1)*2 + (j+1)*2 == brown:
                return [j + 2,i + 2]