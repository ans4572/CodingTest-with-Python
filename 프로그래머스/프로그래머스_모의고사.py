def solution(answers):
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]

    count = [0,0,0]

    p1 *= (len(answers) // len(p1)) + 1
    p2 *= (len(answers) // len(p2)) + 1
    p3 *= (len(answers) // len(p3)) + 1

    for i in range(len(answers)):
        if p1[i] == answers[i]:
            count[0] += 1
        if p2[i] == answers[i]:
            count[1] += 1
        if p3[i] == answers[i]:
            count[2] += 1

    maxNum = max(count)
    answer = []
    for idx,val in enumerate(count):
        if val == maxNum:
            answer.append(idx + 1)

    return answer

