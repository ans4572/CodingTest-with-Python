from itertools import combinations

N, M = list(map(int, input().split()))

homes = []      # 집 위치 저장
chickens = []   # 치킨집 위치 저장
for i in range(N):
    temp = list(map(int, input().split()))
    for idx, val in enumerate(temp):
        if val == 1:
            homes.append([i,idx+1])
        elif val == 2:
            chickens.append([i,idx+1])

ans = N*N*N
comb = list(combinations(chickens, M))  # 생존 치킨집 조합

for choice in comb:
    sum = 0
    # 각 집마다 최소 거리인 치킨집 찾아서 sum에 더해주기
    for home in homes:
        min_dis = N*N
        for c in choice:
            min_dis = min(min_dis, abs(home[0]-c[0]) + abs(home[1]-c[1]))
        sum += min_dis
    ans = min(ans, sum)  # 도시의 최소 치킨 거리 저장

print(ans)

