from itertools import combinations

n = int(input())
xy = [list(map(int,input().split())) for _ in range(n)]

ans = 0
for i in combinations(xy, 3):
    n1 = i[0][1] - i[1][1]
    n2 = i[1][0] - i[2][0]
    n3 = i[1][1] - i[2][1]
    n4 = i[0][0] - i[1][0]

    if n1 * n2 != n3 * n4: ans += 1

print(ans)