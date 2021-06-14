# _*_ coding: utf-8 _*_

def solution(n, t, m, timetable):
    timetable = list(map(lambda x: int(x[:2]) * 60 + int(x[3:]), timetable))   # 분 단위로 변경
    timetable.sort()   # 정렬
    busInfo = [[540, m]]  # 버스 정보 (도착 시간, 남은 좌석)
    for i in range(1, n):
        busInfo.append([busInfo[-1][0] + t, m])
        
    # 버스에 크루들 태우기
    index = 0
    for i in range(n):
        count = 0
        while count < m and index < len(timetable) and timetable[index] <= busInfo[i][0]:
            count += 1
            index += 1
        busInfo[i][1] -= count

    # 마지막 버스에 자리가 남는 경우
    if busInfo[-1][1] > 0:
        return str(busInfo[-1][0] // 60).zfill(2) + ":" + str(busInfo[-1][0] % 60).zfill(2)
    else:
        ret = timetable[index - 1] -1
        return '%02d:%02d' % (ret // 60, ret % 60)

print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))