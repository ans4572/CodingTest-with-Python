import math

def solution(progresses, speeds):
    days = []

    for p in range(len(progresses)):
        days.append(math.ceil((100 - progresses[p]) / speeds[p]))

    answer = []
    stack = []
    for d in days:
        if stack and stack[0] < d:
            answer.append(len(stack))
            stack = []

        stack.append(d)

    #스택에 남아있는 것
    if stack:
        answer.append(len(stack))

    return answer

print(solution([90, 92, 95], [2, 3, 1]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
print(solution([95,97,98], [3, 2, 2]))
