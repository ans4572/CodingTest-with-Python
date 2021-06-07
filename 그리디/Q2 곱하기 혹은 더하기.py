s = input()

ans = int(s[0])
for idx,val in enumerate(s[1:]):
    if ans <= 1 or val <= 1:
        ans += int(val)
    else:
        ans *= int(val)

print(ans)
