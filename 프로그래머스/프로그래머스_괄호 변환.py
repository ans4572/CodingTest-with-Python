def solution(p):
    if p == '':
        return p

    # u와 v로 분리
    openCount, closeCount = 0, 0
    u, v = '', ''
    for idx,value in enumerate(p):
        if value == '(':
            openCount += 1
        else:
            closeCount += 1
        if openCount == closeCount:
            u = p[:idx+1]
            v = p[idx+1:]
            break

    # u가 올바른 괄호 문자열인지 판단
    stack = []
    for i in u:
        if not stack:
            stack.append(i)
            continue
        if i == ")" and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(i)

    # 올바른 괄호가 아닌 경우
    if stack:
        temp = '('
        temp += solution(v)
        temp += ')'
        u = list(u)[1:-1]
        for i in u:
            if i == "(":
                temp += ")"
            else:
                temp += "("
        return temp
    # 올바른 괄호인 경우
    else:
       return u + solution(v)

print(solution("(()())()"))
print(solution(")()("))
print(solution("()))((()"))