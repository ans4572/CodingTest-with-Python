import sys
from itertools import combinations

input = list(input() for _ in range(9))

combi = list(combinations(input, 7))

for i in combi:
    i = list(map(int, i))
    if sum(i) == 100:
        i.sort()
        for j in i:
            print(j)
        sys.exit()