from itertools import permutations

def isPrimaryNum(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    num = list(numbers)
    primaryNum = set([])

    for i in range(1, len(num) + 1):
        for j in permutations(num, i):
            if isPrimaryNum(int(''.join(j))):
                primaryNum.add(int(''.join(j)))

    return len(primaryNum)
