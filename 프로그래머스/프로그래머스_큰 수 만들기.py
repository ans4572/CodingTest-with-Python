def solution(number, k):
    answer = ''
    stack = []

    max = -1
    for idx,n in enumerate(number):
        if k == 0:
            for i in stack:
                answer += i
            for i in number[idx:]:
                answer += i
            break

        if len(stack) == 0:
            stack.append(n)
            max = n
        elif max > n:
            if idx < len(number)-1 and n < number[idx+1]:
                k -= 1
                continue
            else:
                stack.append(n)
        elif max == n:
            stack.append(n)
        else:
            if len(stack) <= k:
                k -= len(stack)
                stack = []
                stack.append(n)
                max = n

    return answer

print(solution("4177252841",4))