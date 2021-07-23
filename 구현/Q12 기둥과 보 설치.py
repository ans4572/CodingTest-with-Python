# 명령어 실행 후 가능한지 확인
def possible(answer):
    # 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
    # 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
    for x,y,a in answer:
        # 기둥인 경우
        if a == 0:
            if y == 0: continue
            elif ([x,y,1] in answer) or ((x > 0) and [x-1,y,1] in answer): continue
            elif (y > 0) and ([x,y-1,0] in answer): continue
            else: return False
        else:
            if ([x, y-1, 0] in answer) or ([x+1,y-1,0] in answer): continue
            elif ([x-1,y,1] in answer) and ([x+1,y,1] in answer): continue
            else: return False

    return True

def solution(n, build_frame):
    answer = []

    for x,y,a,b in build_frame:
        # 삭제하는 경우
        if b == 0:
            answer.remove([x,y,a])
            if not possible(answer):
                answer.append([x,y,a])
        # 설치하는 경우
        else:
            answer.append([x,y,a])
            if not possible(answer):
                answer.remove([x,y,a])

    return sorted(answer)

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))