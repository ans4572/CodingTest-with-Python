N = int(input())
arr = list(map(int,input().split()))
arr.sort()

ans = 0
count = 0  #현재 그룹에 포함된 모험가의 수

for i in arr:       #공포도가 낮은 것부터 확인
    count += 1      #그룹에 해당 모험가 추가
    if count >= i:  #그룹원의 수가 현재 공포도보다 큰 경우 그룹 결정
        ans += 1
        count = 0

print(ans)