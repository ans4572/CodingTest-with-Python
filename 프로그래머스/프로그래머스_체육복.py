def solution(n, lost, reserve):
    student = [0] * (n + 1)

    for i in lost:
        student[i] -= 1
    for i in reserve:
        student[i] += 1

    for idx, val in enumerate(student[:n]):
        if val == -1:
            if student[idx - 1] == 1:
                student[idx - 1] = 0
                student[idx] = 0
                continue
            if student[idx + 1] == 1:
                student[idx + 1] = 0
                student[idx] = 0

    if student[-1] == -1 and student[-2] == 1:
        student[-1] = 0
        student[-2] = 0

    return n - student.count(-1)

print(solution(3,[1,2],[2,3]))