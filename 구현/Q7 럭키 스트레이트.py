N = input()
left = N[:len(N)//2]
left_sum = 0
for i in left:
    left_sum += int(i)
right = N[len(N)//2:]
right_sum = 0
for i in right:
    right_sum += int(i)

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")