def solution(s):
    answer = len(s)

    for i in range(1, len(s)//2 + 1):
        prev = s[:i]   #비교할 문자열
        index, temp = i, 0
        count = 1      #압축할 수 있는 문자열 카운트
        while index < len(s):
            #같은 경우
            if prev == s[index:index+i]:
                count += 1
            else:
                if count > 1:
                    temp += (i+len(str(count)))  #카운트 된 숫자를 문자열로 변환하여 i와 함께 추가
                else:       # 카운트가 1인 경우
                    temp += i
                prev = s[index:index+i]
                count = 1

            index += i

            if index >= len(s):
                if count > 1:
                    temp += (i + 1)
                else:
                    temp += (len(s) % i if len(s) % i != 0 else i)

        answer = min(answer, temp)

    return answer

#print(solution("aabbaccc"))
print(solution("abcabcdede"))