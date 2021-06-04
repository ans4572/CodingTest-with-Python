def solution(record):
    chating = []   # (act, id)로 구성되며 act:1 => enter, act:-1 => out
    user = dict()  # user[id] = userName

    for r in record:
        if r[0] == "L":
            act, id = r.split()
        else:
            act, id, name = r.split()
        if act == "Enter":
            user[id] = name            # user id가 변경되었을 수도 있으므로
            chating.append((1, id))
        elif act == "Leave":
            chating.append((-1, id))
        elif act == "Change":
            user[id] = name

    answer = []
    for act, chatId in chating:
        if act == 1:
            answer.append(user[chatId] + "님이 들어왔습니다.")
        else:
            answer.append(user[chatId] + "님이 나갔습니다.")
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))