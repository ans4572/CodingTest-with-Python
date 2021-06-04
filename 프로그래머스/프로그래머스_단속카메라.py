def solution(routes):
    routes.sort(key=lambda x:x[1])  # 끝나는 지점을 기준으로 정렬
    camera = -30001
    answer = 0

    for route in routes:
        if camera <= route[0]:
            answer += 1
            camera = route[1]

    return answer

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))