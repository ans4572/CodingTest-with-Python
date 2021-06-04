# 문자열을 두 글자씩 분리하는 메서드
def strSplit(str):
    str_list = []
    for idx, val in enumerate(str[:-2]):
        if 'A' <= str[idx] <= 'Z' and 'A' <= str[idx + 1] <= 'Z':
            temp = str[idx] + str[idx + 1]
            str_list.append(temp)
    return str_list

# 분리한 다중 집합을 dict화 시키는 메서드
def strDict(str_list):
    str_dict = dict()
    for i in str_list:
        if i not in str_dict:
            str_dict[i] = 1
        else:
            str_dict[i] += 1
    return str_dict

def solution(str1, str2):
    str1_list = strSplit(str1.upper())
    str2_list = strSplit(str2.upper())

    str1_dict = strDict(str1_list)
    str2_dict = strDict(str2_list)

    intersection, union = 0, 0
    # 교집합 계산
    for k in str1_dict.keys():
        if k in str2_dict:
            intersection += min(str1_dict[k], str2_dict[k])

    # 합집합 계산
    for k in str1_dict.keys():
        # str2_dict에 있다면 가장 큰 값으로 갱신
        if k in str2_dict:
            str2_dict[k] = max(str1_dict[k], str2_dict[k])
        # 없다면 새로 추가
        else:
            str2_dict[k] = str1_dict[k]
    union = sum(str2_dict.values())

    answer = 0
    if intersection == 0 or union == 0:
        answer = 1
    else:
        answer = intersection / union
    return int(answer * 65536)

print(solution("FRANCE", "french"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))