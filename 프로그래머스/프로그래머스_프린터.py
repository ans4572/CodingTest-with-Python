from collections import deque

""" any를 활용했으나 속도는 더 느림
def solution(priorities, location):
    dq = deque()
    for idx, pr in enumerate(priorities):
        dq.append((idx, pr))

    answer = 0
    while True:
        now = dq.popleft()
        if any(now[1] < q[1] for q in dq):
            dq.append(now)
        else:
            answer += 1
            # 요청한 문서가 인쇄된 경우
            if now[0] == location:
                return answer
"""

def solution(priorities, location):
    dq = deque()
    for idx, pr in enumerate(priorities):
        dq.append((idx, pr))

    answer = 0
    while True:
        size = len(dq)
        now = dq.popleft()
        for idx, pr in dq:
            if now[1] < pr:
                dq.append(now)
                break

        # dq의 사이즈가 줄어든 경우
        if size != len(dq):
            answer += 1
            # 요청한 문서가 인쇄된 경우
            if now[0] == location:
                break

    return answer

