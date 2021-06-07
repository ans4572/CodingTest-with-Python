s = input()

arr = []
num = 0
for i in s:
    if i.isalpha():
        arr.append(i)
    else:
        num += int(i)

arr.sort()

if num != 0:
    arr.append(str(num))

print(''.join(arr))