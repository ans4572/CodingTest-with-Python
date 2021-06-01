from functools import cmp_to_key

def cmp(a,b):
    if a+b < b+a:
        return 1
    else:
        return -1

def solution(numbers):
    numbers = map(str, numbers)
    numbers = sorted(numbers, key = cmp_to_key(cmp))

    return ''.join(numbers)

print(solution([6,10,2]))