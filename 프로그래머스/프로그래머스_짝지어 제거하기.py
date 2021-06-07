def solution(s):
    stack = []

    for i in s:
        if len(stack) == 0:
            stack.append(i)
            continue

        # 스택 top과 i가 같은 경우
        if stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    if len(stack) == 0:
        return 1
    else:
        return 0

solution("baabaa")